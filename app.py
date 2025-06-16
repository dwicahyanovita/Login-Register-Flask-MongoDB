from flask import render_template, redirect, session
from functools import wraps
from config import create_app
from models import User

app = create_app()
db = app.config['db']

# dekorator login_required
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    return wrap

# routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def db_login():
    return User(db).login()

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def db_register():
    return User(db).register()

@app.route('/signout')
def signout():
    return render_template('index.html')

@app.route('/signout')
def db_signout():
    return User(db).signout()

@app.route('/home')
@login_required
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
