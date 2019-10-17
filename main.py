from flask import render_template, flash, redirect, url_for, request
from forms import LoginForm, RegistrationForm
from config import app, migrate, db
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse
from models import User
from datetime import datetime


@app.route('/')
@app.route('/home')
@login_required
def home():
    posts = current_user.posts.all()
    return render_template('hello.html', posts = posts)

@app.route('/register', methods = ['GET', 'Post'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        u = User(username = form.username.data, email = form.email.data)
        u.set_password(form.password.data)
        db.session.add(u)
        db.session.commit()
        flash('Congrats your registration was successful')
        return redirect(url_for('login'))
    return render_template('register.html', form = form)


@app.route('/login', methods = ['GET', 'Post'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [ {'author':user, 'body': "Test Post 1"}, {'author':user, 'body': "Test Post 2"}]
    return render_template('user.html', user = user, posts = posts)

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


if "__name__" == "__main__":
	app.run(debug = True)