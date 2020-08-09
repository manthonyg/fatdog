from flask import Flask, jsonify, session, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
from db import db, app, User, Dog
import requests
import json
from forms import RegistrationForm
import click
from flask.cli import with_appcontext


@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()
# Replace the values in .env.example with your values and rename this file to .env:

# FLASK_APP: Entry point of your application (should be wsgi.py).
# FLASK_ENV: The environment to run your app in (either development or production).
# SECRET_KEY: Randomly generated string of characters used to encrypt your app's data.


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/', methods=['GET', 'POST'])
def index():
    previousResults = db.session.query(Dog).order_by(Dog.id).all()
    if request.method == 'POST':

        name = request.form.get('dog-name')
        age = request.form.get('dog-age')
        breed = request.form.get('dog-breed')
        shape = request.form.get('dog-shape')
        activity = request.form.get('dog-activity')
        weight = request.form.get('dog-weight')
        KGS = int(round(int(weight) / int(2.2), 2))
        RER = int(round(int(70) * int((KGS**0.75)), 2))
        MER = round(int(RER) * float(activity))
        breedStats = requests.get(
            f'https://api.thedogapi.com/v1/images/search?breed_ids={breed}')
        user_id = session['id']
        newDog = Dog(name=name, age=age, breed=breed,
                     shape=shape, activity=activity, weight=weight, KGS=KGS, RER=RER, MER=MER, breedStats=breedStats.text, user_id=user_id)

        db.session.add(newDog)
        db.session.commit()

        return render_template('dashboard.html', new_assessment=False, result=True, name=name, weight=weight, KGS=KGS, RER=RER, MER=MER, activity=activity, breedStats=json.loads(newDog.breedStats), username=session['username'], previousResults=previousResults)
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'], assessment=True, previousResults=previousResults)

    return render_template('login.html')


@ app.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm()
    if form.validate_on_submit():

        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        passwordHash = generate_password_hash(password)
        print(username, password, confirm_password)
        newUser = User(username=username, password=passwordHash)
        db.session.add(newUser)
        db.session.commit()
        flash('Account successfully created. Please log in.')
        return render_template('login.html')
    return render_template('register.html', form=form)


@ app.route('/login', methods=['GET', 'POST'])
def login():
    # Forget any username
    session.clear()

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Ensure username was submitted

        incomingUser = User.query.filter_by(username=username).first()
        if not incomingUser or not check_password_hash(incomingUser.password, password):
            flash('Invalid username or password')
            return redirect(url_for('index'))

        session['username'] = request.form['username']
        session['id'] = incomingUser.id

        return redirect(url_for('index'))

    return render_template('login.html')


@ app.route('/logout')
def logout():
    # clear the current user from session
    session['username'] = ''
    flash('You were successfully logged out')
    return render_template('login.html')


@ app.route('/delete_result')
def deleteResult():
    dogId = request.args.get('result-id')
    dog = Dog.query.filter_by(id=dogId).first()
    db.session.delete(dog)
    db.session.commit()
    flash(f"Dog #{dog.name} was successfully deleted")
    return redirect(url_for('index'))


@ app.route('/view_result')
def viewResult():
    previousResults = db.session.query(Dog).order_by(Dog.id).all()
    dogId = request.args.get('dogId')
    dog = Dog.query.filter_by(id=dogId).first()

    print(type(jsonify(dog.breedStats)))
    return render_template('dashboard.html', new_assessment=False, result=True, name=dog.name, weight=dog.weight, KGS=dog.KGS, RER=dog.RER, MER=dog.MER, activity=dog.activity, breedStats=json.loads(dog.breedStats), username=session['username'], previousResults=previousResults)


app.config['DEBUG'] = True

if __name__ == '__main__':
    app.run()
