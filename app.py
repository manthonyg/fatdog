from flask import Flask, session, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
from helpers import calculateReqCalories
from db import db, app, Users, Dogs, Results
import requests
import json


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('dog-name')
        age = request.form.get('dog-age')
        breed = request.form.get('dog-breed')
        shape = request.form.get('dog-shape')
        activity = request.form.get('dog-activity')
        weight = request.form.get('dog-weight')
        user_id = session['id']
        newDog = Dogs(name=name, age=age, breed=breed,
                      shape=shape, activity=activity, weight=weight, user_id=user_id)
        db.session.add(newDog)

        KGS = int(round(int(weight) / int(2.2), 2))
        RER = int(round(int(70) * int((KGS**0.75)), 2))
        MER = round(int(RER) * float(activity))

        dog = Dogs.query.filter_by(
            name=name, age=age, breed=breed, activity=activity).first()

        newResult = Results(suggested_calories=calculateReqCalories(weight, activity),
                            KGS=KGS, RER=RER, MER=MER, user_id=user_id, dog_id=dog.id)

        db.session.add(newResult)
        db.session.commit()

        previousResults = db.session.query(Dogs, Results).outerjoin(
            Results, Dogs.id == Results.dog_id).filter(Results.user_id == session['id']).limit(5).all()

        breedStats = requests.get(
            f'https://api.thedogapi.com/v1/images/search?breed_ids={dog.breed}')

        return render_template('results.html', suggestedCalories=calculateReqCalories(weight, activity), name=name, weight=weight, KGS=KGS, RER=RER, MER=MER, activity=activity, breedStats=json.loads(breedStats.text), username=session['username'], previousResults=previousResults)
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    return render_template('login.html')


@ app.route('/login', methods=['GET', 'POST'])
def login():
    # Forget any username
    session.clear()

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Ensure username was submitted
        if not username:
            return flash("must provide username")
        # Ensure password was submitted
        if not password:
            return flash("must provide password")

        incomingUser = Users.query.filter_by(username=username).first()

        if not incomingUser.username or not check_password_hash(incomingUser.password, password):
            flash('Invalid username or password')
            return redirect(url_for('login'))

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


@ app.route('/register/', methods=['GET', 'POST'])
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
        flash('Account successfully created. Please log in.')
        return render_template('login.html')
    return render_template('register.html')


app.config['DEBUG'] = True

if __name__ == '__main__':
    app.run()
