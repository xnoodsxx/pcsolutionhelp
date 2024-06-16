from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from flask_login import LoginManager, login_user, UserMixin, login_required, logout_user, current_user
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from datetime import datetime
import os
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = 'asagiriDev'
login_manager = LoginManager(app)
login_manager.login_view = 'login'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'Database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'avatars')
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f"Feedback('{self.email}', '{self.subject}', '{self.date_posted}')"
    
class FeedbackForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Тема', validators=[DataRequired()])
    message = TextAreaField('Сообщение', validators=[DataRequired()])
    submit = SubmitField('Отправить')

@app.route("/feedback", methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        feedback = Feedback(email=form.email.data, subject=form.subject.data, message=form.message.data)
        db.session.add(feedback)
        db.session.commit()
        flash('Ваше сообщение отправлено!', 'success')
        return redirect(url_for('index'))
    return render_template('feedback.html', title='Обратная связь', form=form)

@app.route("/admin/feedbacks")
@login_required
def admin_feedbacks():
    if current_user.is_authenticated and current_user.is_admin:
        feedbacks = Feedback.query.order_by(Feedback.date_posted.desc()).all()
        return render_template('admin_feedbacks.html', title='Сообщения пользователей', feedbacks=feedbacks)
    else:
        flash('Доступ запрещен. Только для администратора.', 'danger')
        return redirect(url_for('login'))
    
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    build_id = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    final_price = db.Column(db.Float, nullable=False)


# Маршрут для отображения страницы заказов
@app.route('/orders')
def view_orders():
    if current_user.is_authenticated and current_user.is_admin:
        return render_template('orders.html')
    else:
        # Обработка случая, если пользователь не аутентифицирован или не является администратором
        return render_template('access_denied.html')  # Замените 'access_denied.html' на ваш шаблон для отказа в доступе

# Маршрут для получения заказов из базы данных
@app.route('/get_orders')
def get_orders_from_database():
    if current_user.is_authenticated and current_user.is_admin:
        # Получаем заказы из базы данных
        orders = Order.query.all()
        # Создаем словарь для хранения информации о заказах
        orders_data = []
        for order in orders:
            # Получаем пользователя по его user_id
            user = User.query.get(order.user_id)
            # Добавляем информацию о заказе в список
            orders_data.append({
                'id': order.id,
                'user': user.username if user else 'Unknown',
                'address': order.address,
                'total_price': order.total_price,
                'final_price': order.final_price
            })
        # Возвращаем данные о заказах в формате JSON
        return jsonify(orders_data)
    else:
        # Возвращаем ошибку доступа, если пользователь не является администратором
        return jsonify({'error': 'Access denied'}), 403  # Ошибка 403 - доступ запрещен
    
# Маршрут для отображения подробностей о заказе
@app.route('/order_details/<int:order_id>')
def order_details(order_id):
    # Здесь ваш код для получения подробностей о заказе по его ID из базы данных
    order = Order.query.get(order_id)
    if order:
        # Получаем компоненты сборки по ID сборки из заказа
        build = Build.query.get(order.build_id)
        if build:
            build_components = [
                build.processor, build.videocard, build.ram, build.motherboard,
                build.psu, build.harddrive, build.case, build.keyboard,
                build.mouse, build.monitor, build.coolingsystem
            ]
            return render_template('order_details.html', order=order, build_components=build_components)
        else:
            return render_template('order_not_found.html')  # Создайте шаблон для сообщения о том, что сборка не найдена
    else:
        return render_template('order_not_found.html')  # Создайте шаблон для сообщения о том, что заказ не найден

# Маршрут для обновления информации об отдельном заказе (опционально)
@app.route('/update_order/<int:order_id>', methods=['POST'])
def update_order(order_id):
    # Здесь ваш код для обновления заказа (например, изменение статуса заказа и т. д.)
    return jsonify({'message': 'Order updated successfully'})  # Пример ответа, можно заменить на что-то более конкретное   

@app.route('/submit_order', methods=['POST'])
def submit_order():
    try:
        data = request.json
        print("Received data:", data)  # Выводим полученные данные для отладки

        # Проверяем, что все необходимые поля присутствуют в данных
        required_fields = ['email', 'address', 'totalPrice', 'build_id', 'final_price']
        for field in required_fields:
            if field not in data:
                print(f"Missing required field: {field}")  # Выводим отладочное сообщение
                return jsonify({'error': f'Missing required field: {field}'}), 400  # Ошибка 400 - неверный запрос

        # Извлекаем данные из запроса
        email = data['email']
        address = data['address']
        total_price = data['totalPrice']  # Извлекаем общую стоимость из данных заказа
        build_id = data['build_id']
        final_price = data['final_price']  # Извлекаем итоговую стоимость из данных заказа

        # Получаем ID текущего пользователя
        user_id = current_user.id

        # Создаем заказ и сохраняем в базе данных
        order = Order(user_id=user_id, email=email, build_id=build_id, address=address, total_price=total_price, final_price=final_price)
        db.session.add(order)
        db.session.commit()

        return jsonify({'success': True, 'message': 'Order saved successfully!'})
    except Exception as e:
        print("Error:", e)  # Выводим ошибку в консоль
        return jsonify({'error': 'Internal Server Error'}), 500  # Ошибка 500 - внутренняя ошибка сервера
    
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    avatar = db.Column(db.String(120), nullable=True)
    is_admin = db.Column(db.Boolean, default=False)

    # Измененное имя обратной связи для отношения builds
    user_builds = db.relationship('Build', backref='user', lazy=True)
    
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(120), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
 
def save_image(image):
    filename = secure_filename(image.filename)
    filepath = os.path.join(app.root_path, 'static/uploads', filename)
    image.save(filepath)
    return filename

class MyAdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))
        
    def on_model_change(self, form, model, is_created):
        if 'password' in form and form.password.data:
            model.password = generate_password_hash(form.password.data)

class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))

# Изменяем используемый шаблон на 'admin_home.html'
admin = Admin(app, name='Панель Администратора', template_mode='bootstrap3', index_view=AdminIndexView(template='admin_home.html'))
admin.add_view(MyAdminModelView(User, db.session, name='User_Admin_Panel'))
admin.add_view(AdminModelView(News, db.session, name='News_Admin_Panel'))

class NewsForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    image = FileField('Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField('Create News')

class Build(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    processor = db.Column(db.String(100))
    videocard = db.Column(db.String(100))
    ram = db.Column(db.String(100))
    motherboard = db.Column(db.String(100))
    psu = db.Column(db.String(100))
    harddrive = db.Column(db.String(100))
    case = db.Column(db.String(100))
    keyboard = db.Column(db.String(100))
    mouse = db.Column(db.String(100))
    monitor = db.Column(db.String(100))
    coolingsystem = db.Column(db.String(100))
    total_price = db.Column(db.Float, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Processor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    cores = db.Column(db.Integer, nullable=False)
    threads = db.Column(db.Integer, nullable=False)
    base_clock = db.Column(db.Float, nullable=False)
    boost_clock = db.Column(db.Float, nullable=False)
    socket = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    tdp = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'manufacturer': self.manufacturer,
            'cores': self.cores,
            'threads': self.threads,
            'base_clock': self.base_clock,
            'boost_clock': self.boost_clock,
            'socket': self.socket,
            'price': self.price,
            'tdp': self.tdp  # Включено поле TDP в сериализацию
        }
    
    def is_compatible_with_motherboard(self, motherboard):
        """
        Проверяет, совместим ли данный процессор с данной материнской платой.

        Args:
            motherboard (Motherboard): Объект материнской платы.

        Returns:
            bool: True, если совместим, False в противном случае.
        """
        # Проверка совместимости по сокету процессора и материнской платы
        if self.socket != motherboard.socket:
            return False
        return True
    
class Videocard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    interface = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    chipset_brand = db.Column(db.String(100), nullable=False)
    core_clock = db.Column(db.Float, nullable=False)  # Добавлено поле для базовой частоты ядра
    boost_clock = db.Column(db.Float, nullable=False)  # Добавлено поле для максимальной частоты Boost
    vram_type = db.Column(db.String(100), nullable=False)  # Тип видеопамяти
    vram_capacity = db.Column(db.String(100), nullable=False)  # Объем видеопамяти

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'manufacturer': self.manufacturer,
            'memory': self.memory,
            'interface': self.interface,
            'price': self.price,
            'chipset_brand': self.chipset_brand,
            'core_clock': self.core_clock,
            'boost_clock': self.boost_clock,
            'vram_type': self.vram_type,
            'vram_capacity': self.vram_capacity
        }


    def is_compatible_with_motherboard(self, motherboard):
        """
        Проверяет, совместима ли данная видеокарта с данной материнской платой.

        Args:
            motherboard (Motherboard): Объект материнской платы.

        Returns:
            bool: True, если совместима, False в противном случае.
        """
        # Проверка совместимости по интерфейсу видеокарты и материнской платы
        if self.interface != motherboard.pci_express_version:
            return False
        return True

class Motherboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    socket = db.Column(db.String(100), nullable=False)
    form_factor = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    memory_type_support = db.Column(db.String(100), nullable=False)
    memory_slots = db.Column(db.Integer, nullable=False)
    max_memory = db.Column(db.String(100), nullable=False)
    pci_express_slots = db.Column(db.Integer, nullable=False)
    chipset = db.Column(db.String(100), nullable=False)  # Чипсет материнской платы

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'manufacturer': self.manufacturer,
            'socket': self.socket,
            'form_factor': self.form_factor,
            'price': self.price,
            'memory_type_support': self.memory_type_support,
            'memory_slots': self.memory_slots,
            'max_memory': self.max_memory,
            'pci_express_slots': self.pci_express_slots,
            'chipset': self.chipset
        }


    def is_compatible_with_processor(self, processor):
        """
        Проверяет, совместима ли данная материнская плата с данным процессором.

        Args:
            processor (Processor): Объект процессора.

        Returns:
            bool: True, если совместима, False в противном случае.
        """
        # Проверка совместимости по сокету процессора и материнской платы
        if self.socket != processor.socket:
            return False
        return True

class PowerSupplyUnit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    wattage = db.Column(db.Integer, nullable=False)
    efficiency_rating = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    modular = db.Column(db.Boolean, nullable=False)  # Поддержка модульного кабельного управления

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'manufacturer': self.manufacturer,
            'wattage': self.wattage,
            'efficiency_rating': self.efficiency_rating,
            'price': self.price,
            'modular': self.modular
        }


    def is_compatible_with_videocard(self, videocard):
        """
        Проверяет, подходит ли данный блок питания для данной видеокарты.

        Args:
            videocard (Videocard): Объект видеокарты.

        Returns:
            bool: True, если совместим, False в противном случае.
        """
        # Проверка на минимальную мощность блока питания для данной видеокарты
        if self.wattage < videocard.power_requirement:
            return False
        return True


class RAM(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.String(100), nullable=False)
    speed = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    memory_type = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'manufacturer': self.manufacturer,
            'capacity': self.capacity,
            'speed': self.speed,
            'price': self.price,
            'memory_type': self.memory_type
        }

class HardDrive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.String(100), nullable=False)
    interface = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    form_factor = db.Column(db.String(100), nullable=False)  # Форм-фактор жесткого диска

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'manufacturer': self.manufacturer,
            'capacity': self.capacity,
            'interface': self.interface,
            'price': self.price,
            'form_factor': self.form_factor
        }


class Case(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    form_factor = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    usb_ports = db.Column(db.Integer, nullable=False)  # Количество USB портов на корпусе
    drive_bays = db.Column(db.String(100), nullable=False)  # Количество отсеков для накопителей

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'manufacturer': self.manufacturer,
            'form_factor': self.form_factor,
            'price': self.price,
            'usb_ports': self.usb_ports,
            'drive_bays': self.drive_bays
        }


class Keyboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    connectivity = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    backlight = db.Column(db.Boolean, nullable=False)  # Наличие подсветки клавиатуры

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'manufacturer': self.manufacturer,
            'connectivity': self.connectivity,
            'price': self.price,
            'backlight': self.backlight
        }


class Mouse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    connectivity = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    dpi = db.Column(db.Integer, nullable=False)  # Чувствительность мыши (DPI)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'manufacturer': self.manufacturer,
            'connectivity': self.connectivity,
            'price': self.price,
            'dpi': self.dpi
        }


class CoolingSystem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    fan_size = db.Column(db.Integer, nullable=False)  # Размер вентилятора в мм

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'manufacturer': self.manufacturer,
            'type': self.type,
            'price': self.price,
            'fan_size': self.fan_size
        }


class Monitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    display_size = db.Column(db.String(100), nullable=False)
    resolution = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    refresh_rate = db.Column(db.Integer, nullable=False)
    panel_type = db.Column(db.String(100), nullable=False)  # Тип панели (TN, IPS, VA)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'manufacturer': self.manufacturer,
            'display_size': self.display_size,
            'resolution': self.resolution,
            'price': self.price,
            'refresh_rate': self.refresh_rate,
            'panel_type': self.panel_type
        }



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) if user_id is not None else None

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def send_email(name, email, message):
    sender = 'your_email@example.com'
    receiver = 'receiver_email@example.com'
    subject = 'New Contact Form Submission'
    body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('your_email@example.com', 'your_password')
        server.sendmail(sender, receiver, msg.as_string())

@app.route('/')
def index():
    # Извлечение последних 4 новостей из базы данных
    latest_news = News.query.order_by(News.id.desc()).limit(4).all()
    return render_template('index.html', latest_news=latest_news, num_news=len(latest_news))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        if not username or not password or not email:
            flash('Please fill in all fields.')
            return render_template('register.html')

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('User with this username already exists.')
            return render_template('register.html')

        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash('User with this email is already registered.')
            return render_template('register.html')

        try:
            new_user = User(
                username=username,
                password=generate_password_hash(password),
                email=email
            )
            db.session.add(new_user)
            db.session.commit()

            flash('Registration successful. You can now log in.')
            return redirect(url_for('login'))

        except IntegrityError:
            db.session.rollback()
            flash('Username or email already exists.')
        except Exception as e:
            db.session.rollback()
            flash(f'Error during registration: {str(e)}')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user:
            app.logger.info(f'User found: {user.username}, {user.password}, {user.id}')
            
            if check_password_hash(user.password, password):
                login_user(user)
                flash('Login successful.')
                return redirect(url_for('dashboard'))
            else:
                app.logger.warning(f'Incorrect password for user: {user.username}')
                flash('Incorrect password.')
        else:
            app.logger.warning(f'User not found with username: {username}')
            flash('User not found.')

    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    user_builds = Build.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', user=current_user, builds=user_builds)

@app.route('/update_avatar', methods=['POST'])
@login_required
def update_avatar():
    if 'avatar' in request.files:
        avatar = request.files['avatar']
        if avatar.filename != '':
            if allowed_file(avatar.filename):
                filename = secure_filename(avatar.filename)
                avatar.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                current_user.avatar = filename
                db.session.commit()
                flash('Avatar updated successfully.')
            else:
                flash('Invalid file type. Allowed file types are png, jpg, jpeg, gif.')
        else:
            flash('No file selected.')
    else:
        flash('No avatar uploaded.')
    return redirect(url_for('dashboard'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out.')
    return redirect(url_for('index'))

@app.route('/create_news', methods=['GET', 'POST'])
@login_required
def create_news():
    if not current_user.is_admin:
        flash('You do not have permission to create news.')
        return redirect(url_for('dashboard'))

    form = NewsForm()

    if form.validate_on_submit():
        # Save image file if provided
        image_file = None
        if form.image.data:
            image_file = save_image(form.image.data)

        news = News(title=form.title.data, content=form.content.data, image=image_file)
        db.session.add(news)
        db.session.commit()
        flash('News created successfully.')
        return redirect(url_for('news'))

    return render_template('create_news.html', form=form)

@app.route('/news')
def news():
    news_list = News.query.order_by(News.created_at.desc()).all()
    return render_template('news.html', news_list=news_list)

@app.route('/news/<int:news_id>')
def view_news(news_id):
    news_item = News.query.get_or_404(news_id)
    return render_template('view_news.html', news_item=news_item)

@app.route('/configurator')
@login_required
def configurator():
    videocards = Videocard.query.all()
    processors = Processor.query.all() 
    motherboards = Motherboard.query.all()
    psus = PowerSupplyUnit.query.all()
    ram = RAM.query.all()
    harddrives = HardDrive.query.all()
    cases = Case.query.all()
    keyboards = Keyboard.query.all()
    mice = Mouse.query.all()
    monitors = Monitor.query.all()
    coolingsystems = CoolingSystem.query.all()

    return render_template(
        'configurator.html', 
        user=current_user, 
        videocards=videocards,
        processors=processors, 
        motherboards=motherboards,
        psus=psus,
        ram=ram,
        harddrives=harddrives,
        cases=cases,
        keyboards=keyboards,
        mice=mice,
        monitors=monitors,
        coolingsystems=coolingsystems
    )


@app.route('/save_build', methods=['POST'])
def save_build():
    try:
        data = request.get_json()
        print("Received JSON data:", data)

        user_id = data.get('user_id')
        print("User ID:", user_id)

        # Получаем общую цену сборки
        total_price = data.get('total_price', 0.0)

        new_build = Build(
            name=data.get('build_name'),
            processor=data.get('processor'),
            videocard=data.get('videocard'), 
            ram=data.get('ram'),
            motherboard=data.get('motherboard'),
            psu=data.get('psu'),
            harddrive=data.get('harddrive'),
            case=data.get('case'),
            keyboard=data.get('keyboard'),
            mouse=data.get('mouse'),
            monitor=data.get('monitor'),
            coolingsystem=data.get('coolingsystem'),
            user_id=user_id,
            total_price=total_price  # Передаем общую цену сборки
        )

        print("New build data:", new_build.__dict__)
        db.session.add(new_build)
        db.session.commit()
        return jsonify({'message': 'Сборка успешно сохранена'})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'message': str(e)}), 500

@app.route('/build/<int:build_id>')
def build(build_id):
    # Получение информации о сборке с заданным идентификатором build_id из базы данных
    build_info = Build.query.get_or_404(build_id)
    return render_template('build.html', build=build_info, total_price=build_info.total_price)  # Передаем total_price в шаблон

# Маршрут для удаления сборки
@app.route('/delete_build/<int:build_id>', methods=['DELETE'])
def delete_build(build_id):
    build = Build.query.get_or_404(build_id)  # Находим сборку по ID или возвращаем ошибку 404
    try:
        db.session.delete(build)  # Удаляем сборку из базы данных
        db.session.commit()
        return jsonify({'message': f'Сборка с ID {build_id} успешно удалена'})
    except:
        return jsonify({'message': 'Произошла ошибка при удалении сборки'}), 500


@app.route('/change_build_name/<int:build_id>', methods=['POST'])
@login_required
def change_build_name(build_id):
    if request.method == 'POST':
        new_name = request.json.get('new_name')  # Получаем новое имя из запроса
        build = Build.query.get(build_id)
        if build and build.user_id == current_user.id:
            build.name = new_name  # Обновляем имя сборки
            db.session.commit()  # Сохраняем изменения в базе данных
            return jsonify({'message': 'Имя сборки успешно изменено'})
    return jsonify({'error': 'Ошибка при изменении имени сборки'}), 400  # Возвращаем ошибку 400 в случае проблемы

@app.route('/contactus', methods=['GET', 'POST'])
def contactus():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']


        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contactus'))
    
    return render_template('feedback.html')

# Маршрут для получения данных о комплектующем по его ID
@app.route('/component_info/<int:component_id>')
def component_info(component_id):
    component = None
    component_type = request.args.get('type')  # Получаем тип комплектующего из параметра запроса

    if component_type == 'processor':
        component = Processor.query.get_or_404(component_id)
    elif component_type == 'videocard':
        component = Videocard.query.get_or_404(component_id)
    elif component_type == 'motherboard':
        component = Motherboard.query.get_or_404(component_id)
    elif component_type == 'powersupplyunit':
        component = PowerSupplyUnit.query.get_or_404(component_id)
    elif component_type == 'ram':
        component = RAM.query.get_or_404(component_id)
    elif component_type == 'harddrive':
        component = HardDrive.query.get_or_404(component_id)
    elif component_type == 'case':
        component = Case.query.get_or_404(component_id)
    elif component_type == 'keyboard':
        component = Keyboard.query.get_or_404(component_id)
    elif component_type == 'mouse':
        component = Mouse.query.get_or_404(component_id)
    elif component_type == 'coolingsystem':
        component = CoolingSystem.query.get_or_404(component_id)
    elif component_type == 'monitor':
        component = Monitor.query.get_or_404(component_id)
    else:
        return jsonify({'error': 'Invalid component type'}), 400

    if component:
        return jsonify(component.serialize())
    else:
        return jsonify({'error': 'Component not found'}), 404


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template("contact.html")

@app.route('/about', methods=['GET', 'POST'])
def aboutus():
    return render_template("aboutus.html")

@app.route('/get_processors')
def get_processors():
    processors = Processor.query.all()
    return jsonify([processor.serialize() for processor in processors])

@app.route('/get_videocards')
def get_videocards():
    videocards = Videocard.query.all()
    return jsonify([videocard.serialize() for videocard in videocards])

@app.route('/get_motherboards')
def get_motherboards():
    motherboards = Motherboard.query.all()
    return jsonify([motherboard.serialize() for motherboard in motherboards])

@app.route('/get_psus')
def get_psus():
    psus = PowerSupplyUnit.query.all()
    return jsonify([psu.serialize() for psu in psus])
    
@app.route('/get_ram')
def get_ram():
    ram = RAM.query.all()
    return jsonify([ram_module.serialize() for ram_module in ram])

@app.route('/get_harddrives')
def get_harddrives():
    harddrives = HardDrive.query.all()
    return jsonify([harddrive.serialize() for harddrive in harddrives])

@app.route('/get_cases')
def get_cases():
    cases = Case.query.all()
    return jsonify([case.serialize() for case in cases])

@app.route('/get_keyboards')
def get_keyboards():
    keyboards = Keyboard.query.all()
    return jsonify([keyboard.serialize() for keyboard in keyboards])

@app.route('/get_mice')
def get_mice():
    mice = Mouse.query.all()
    return jsonify([mouse.serialize() for mouse in mice])

@app.route('/get_monitors')
def get_monitors():
    monitors = Monitor.query.all()
    return jsonify([monitor.serialize() for monitor in monitors])

@app.route('/get_coolingsystems')
def get_coolingsystems():
    coolingsystems = CoolingSystem.query.all()
    return jsonify([coolingsystem.serialize() for coolingsystem in coolingsystems])

@app.route('/get_build_components/<int:buildId>')
def get_build_components(buildId):
    # Находим сборку в базе данных по её ID
    build = Build.query.get_or_404(buildId)

    # Получаем цены компонентов
    processor_price = Processor.query.filter_by(name=build.processor).first().price if build.processor else None
    videocard_price = Videocard.query.filter_by(name=build.videocard).first().price if build.videocard else None
    ram_price = RAM.query.filter_by(name=build.ram).first().price if build.ram else None
    motherboard_price = Motherboard.query.filter_by(name=build.motherboard).first().price if build.motherboard else None
    psu_price = PowerSupplyUnit.query.filter_by(name=build.psu).first().price if build.psu else None
    harddrive_price = HardDrive.query.filter_by(name=build.harddrive).first().price if build.harddrive else None
    case_price = Case.query.filter_by(name=build.case).first().price if build.case else None
    keyboard_price = Keyboard.query.filter_by(name=build.keyboard).first().price if build.keyboard else None
    mouse_price = Mouse.query.filter_by(name=build.mouse).first().price if build.mouse else None
    monitor_price = Monitor.query.filter_by(name=build.monitor).first().price if build.monitor else None
    coolingsystem_price = CoolingSystem.query.filter_by(name=build.coolingsystem).first().price if build.coolingsystem else None

    # Возвращаем данные с ценами компонентов
    return jsonify({
        'id': build.id,
        'name': build.name,
        'processor': build.processor,
        'processor_price': processor_price,
        'videocard': build.videocard,
        'videocard_price': videocard_price,
        'ram': build.ram,
        'ram_price': ram_price,
        'motherboard': build.motherboard,
        'motherboard_price': motherboard_price,
        'psu': build.psu,
        'psu_price': psu_price,
        'harddrive': build.harddrive,
        'harddrive_price': harddrive_price,
        'case': build.case,
        'case_price': case_price,
        'keyboard': build.keyboard,
        'keyboard_price': keyboard_price,
        'mouse': build.mouse,
        'mouse_price': mouse_price,
        'monitor': build.monitor,
        'monitor_price': monitor_price,
        'coolingsystem': build.coolingsystem,
        'coolingsystem_price': coolingsystem_price,
        'user_id': build.user_id
    })


@app.route('/check_compatibility', methods=['POST'])
def check_compatibility():
    if request.method == 'POST':
        build_data = request.json
        processor = build_data['processor']
        gpu = build_data['gpu']
        ram = build_data['ram']
        motherboard = build_data['motherboard']
        psu = build_data['psu']
        
        
        # Возвращаем сообщение о совместимости или несовместимости
        return jsonify({'message': 'Совместимость проверена'})
    
@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy_policy.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
