from flask import render_template, flash, redirect, url_for, request
from config import app, migrate, db
from werkzeug.urls import url_parse
from models import Worker, Availability
from forms import AddWorker, EditAvailability, RegistrationForm, LoginForm
from models import Worker, Availability, User
from flask_login import current_user, login_user, login_required, logout_user

@app.route('/')
@app.route('/home')
def home():
    users = User.query.all()
    return render_template('hello.html', users = users)

@app.route('/team')
def team():
    workers = Worker.query.all()
    return render_template('team.html', workers = workers)

@app.route('/add_worker', methods = ['GET', 'POST'])
@login_required
def add_worker():
    if current_user.is_gm():
        form = AddWorker()
        if form.validate_on_submit():
            w = Worker(first_name = form.first_name.data, last_name = form.last_name.data,
            position = form.position.data)
            a = Availability(worker = w)
            db.session.add(w)
            db.session.commit()
            flash('Worker ' + w.first_name + 'was added!')
            return redirect(url_for('home'))
        return render_template('add_worker.html', form = form)
    flash('You must be a GM to do that')
    return redirect(url_for('home'))

@app.route('/edit_worker', methods = ['GET', 'POST'])
@login_required
def edit_worker():
    if current_user.is_manager():
        workers = Worker.query.all()
        return render_template('select_worker.html', workers = workers)
    flash('You must be a manager to access this page')
    return redirect(url_for('home'))

@app.route('/worker/<first_name>',  methods = ['GET', 'POST'])
def worker(first_name):
    worker = Worker.query.filter_by(first_name=first_name).first_or_404()
    form = AddWorker()
    if form.validate_on_submit():
        worker.first_name = form.first_name.data
        worker.last_name = form.last_name.data
        worker.position = form.position.data
        db.session.commit()
        flash('Worker Info Edited!')
        return redirect(url_for('home'))
    form.first_name.data= worker.first_name
    form.last_name.data = worker.last_name
    form.position.data = worker.position
    return render_template('add_worker.html', form = form, worker = worker.first_name)

@app.route('/edit_availability/<worker>', methods = ['GET', 'POST'])
def edit_availability(worker):
    form = EditAvailability()
    worker = Worker.query.filter_by(first_name = worker).first_or_404()
    current_availability = worker.availabilities.first()
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
    
    form.monday.data = current_availability.monday
    form.tuesday.data = current_availability.tuesday
    form.wednesday.data = current_availability.wednesday
    form.thursday.data = current_availability.thursday
    form.friday.data = current_availability.friday
    form.saturday.data = current_availability.saturday
    form.sunday.data = current_availability.sunday
    return render_template('edit_availability.html', form = form, worker = worker)

@app.route('/add_schedule', methods = ['GET', 'POST'])
@login_required
def add_schedule():
    if current_user.is_manager():
        return render_template('add_schedule.html')
    return redirect(url_for('home'))

@app.route('/register', methods = ['GET', 'Post'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        w = Worker.query.filter_by(first_name = form.name.data.split(' ')[0]).first()
        u = User(username = form.username.data, worker = w)
        u.set_password(form.password.data)
        db.session.add(u)
        db.session.commit()
        flash('Congrats your registration was successful')
        return redirect(url_for('home'))
    return render_template('register.html', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
#    if current_user.is_authenticated:
 #       return redirect(url_for('home'))
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
    return render_template('user.html', user = user)

if "__name__" == "__main__":
    app.run(debug = True)