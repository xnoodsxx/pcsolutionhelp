from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
from flask_login import LoginManager, login_user, UserMixin, login_required, logout_user, current_user
from flask_migrate import Migrate
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
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    avatar = db.Column(db.String(120), nullable=True)

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

        avatar = request.files['avatar']

        if avatar and allowed_file(avatar.filename):
            avatar_filename = f'{username}_{secure_filename(avatar.filename)}'
        else:
            avatar_filename = None

        try:
            new_user = User(
                username=username,
                password=generate_password_hash(password),
                email=email,
                avatar=avatar_filename
            )

            db.session.add(new_user)
            db.session.commit()

            if avatar_filename:
                avatar.save(os.path.join(app.config['UPLOAD_FOLDER'], avatar_filename))

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
    return render_template('dashboard.html', user=current_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
