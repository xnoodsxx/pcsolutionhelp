from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.exc import IntegrityError
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin.model import typefmt
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from flask_login import LoginManager, login_user, UserMixin, login_required, logout_user, current_user
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from datetime import datetime
import os

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
    
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

admin = Admin(app, name='Admin Panel', template_mode='bootstrap3', index_view=AdminIndexView())
admin.add_view(MyAdminModelView(User, db.session, name='User_Admin_Panel'))
admin.add_view(AdminModelView(News, db.session, name='News_Admin_Panel'))

class NewsForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Create News')

class Build(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    processor = db.Column(db.String(100))
    gpu = db.Column(db.String(100))
    ram = db.Column(db.String(100))
    motherboard = db.Column(db.String(100))
    psu = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) if user_id is not None else None

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

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

        except Exception as e:
            flash(f'Error during registration: {str(e)}')
            db.session.rollback()

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
        # Создайте новость и добавьте ее в базу данных
        news = News(title=form.title.data, content=form.content.data)
        db.session.add(news)
        db.session.commit()
        flash('News created successfully.')

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
    return render_template('configurator.html', user=current_user)

@app.route('/save_build', methods=['POST'])
def save_build():
    if request.method == 'POST':
        build_data = request.json
        # Добавляем user_id при создании сборки
        build_data['user_id'] = current_user.id
        build = Build(**build_data)
        db.session.add(build)
        try:
            db.session.commit()
            return jsonify({'message': 'Сборка успешно сохранена'}), 200
        except IntegrityError as e:
            db.session.rollback()
            return jsonify({'error': 'Ошибка сохранения сборки'}), 500
    else:
        return jsonify({'error': 'Метод не поддерживается'}), 405
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
