from flask import Flask, session, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fatdogdb.sqlite3'
db = SQLAlchemy(app)

db.Model.metadata.reflect(db.engine)


class Users(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/1.0/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/')
@login_required
def index():
    if 'username' in session:
        print("Total number of users is", Users.query.count())
        return render_template('dashboard.html', username=session['username'])
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Forget any user_id
    session.clear()

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        passwordHash = generate_password_hash(password)
        # Ensure username was submitted
        if not username:
            return flash("must provide username")
        # Ensure password was submitted
        if not password:
            return flash("must provide password")
        incomingUser = Users.query.filter_by(username=username)
        incomingPassword = Users.query.filter_by(password=passwordHash)
        print(incomingUser, incomingPassword)

        if not incomingUser or not incomingPassword:
            flash('No matching user')
            return render_template('login.html')

        session['username'] = request.form['username']
        return redirect(url_for('index'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    # clear the current user from session
    session['username'] = ''
    flash('You were successfully logged out')
    return render_template('login.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        passwordHash = generate_password_hash(password)

        if not username:
            flash('Invalid username')
        if password != confirm_password:
            flash('Passwords must match')
        if not password:
            flash('Invalid password')

        newUser = Users(username=username, password=passwordHash)
        db.session.add(newUser)
        db.session.commit()
        return render_template('login.html')
    return render_template('register.html')


app.config['DEBUG'] = True

if __name__ == '__main__':
    app.run()
