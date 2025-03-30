from flask import Blueprint, flash, redirect, url_for, session, request, render_template

auth_bp = Blueprint('auth', __name__)

USERS = {
    "admin": {"password": "admin123", "email": "admin@example.com", "address": "123 Main St"},
    "user1": {"password": "password1", "email": "user1@example.com", "address": "456 Oak Ave"}
}

@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']
        
        if username in USERS and USERS[username]['password'] == password:
            session["username"] = username
            session["email"] = USERS[username]['email']
            return redirect(url_for('chat.home'))
        flash("Username and Password Mismatch", "danger")
    return redirect(url_for('auth.index'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['name']
        if username in USERS:
            flash("Username already exists", "danger")
            return redirect(url_for('auth.register'))
        
        USERS[username] = {
            "password": request.form['Password'],
            "email": request.form['Email'],
            "address": request.form['address']
        }
        flash("Registration Successful", "success")
        return redirect(url_for('auth.index'))
    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.index'))

@auth_bp.route('/')
def index():
    return render_template('index.html')