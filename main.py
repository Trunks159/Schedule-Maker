from flask import render_template, flash, redirect, url_for, request, jsonify
from config import app, db
from werkzeug.urls import url_parse
from forms import EditAvailability, RegistrationForm, LoginForm
from models import User
from flask_login import current_user, login_user, login_required, logout_user


@app.route('/')
@app.route('/home')
def home():
    # homes screen lists all user's names and avatars
    users = User.query.all()
    return render_template('index.html', users=users)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        u = User(username=form.username.data, first_name=form.first_name.data,
                 last_name=form.last_name.data)
        positions = {'manager': 1, 'crew': 0}
        u.position = 0 if form.position.data.lower() == 'crew' else 1
        u.set_password(form.password.data)
        db.session.add(u)
        db.session.commit()
        flash('Congrats your registration was successful')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
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
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)


'''in progress this next view'''
@app.route('/users')
def users():
    users_list = User.query.all()
    users = []
    for user in users_list:
        users.append(user.to_json())
    return jsonify({"users": users, 'current_user': current_user.to_json()})


@app.route('/getUrl')
def getUrl(x):
    return jsonify({'url': url_for(x)})


'''
@app.route('/edit_availability/<username>', methods = ['GET', 'POST'])
def edit_availability(username):
    form = EditAvailability()
    user = User.query.filter_by(username = username).first_or_404()
    if form.validate_on_submit():
        current_availability.monday = form.monday.data
        current_availability.tuesday = form.tuesday.data
        current_availability.wednesday = form.wednesday.data
        current_availability.thursday = form.thursday.data
        current_availability.friday = form.friday.data
        current_availability.saturday = form.saturday.data
        current_availability.sunday = form.sunday.data
        db.session.commit()
        flash('Worker Availability Edited!')
        return redirect(url_for('home'))
    current_availability = user.availability
    form.monday.data = current_availability[0]
    form.tuesday.data = current_availability[1]
    form.wednesday.data = current_availability[2]
    form.thursday.data = current_availability[3]
    form.friday.data = current_availability[4]
    form.saturday.data = current_availability[5]
    form.sunday.data = current_availability[6]
    return render_template('edit_availability.html', form = form, user = user)
'''
'''
THIS IS ALL GM STUFF BELOW
'''
@app.route('/edit_worker', methods=['GET', 'POST'])
@login_required
# if you're a gm this basically gives you a list of the workers and
# a link to edit them, you'll be redirected if not a gm
def edit_worker():
    if current_user.worker.position:
        workers = Worker.query.all()
        return render_template('select_worker.html', workers=workers)
    flash('You must be a manager to access this page')
    return redirect(url_for('home'))


if "__name__" == "__main__":
    app.debug = True
    app.run()
