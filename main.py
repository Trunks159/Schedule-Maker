from flask import render_template, flash, redirect, url_for, request
from config import app, migrate, db
from werkzeug.urls import url_parse
from models import Worker
from forms import AddWorker, EditAvailability


@app.route('/')
@app.route('/home')
def home():
    workers = Worker.query.all()
    return render_template('hello.html', workers = workers)

@app.route('/team')
def team():
    workers = Worker.query.all()
    return render_template('team.html', workers = workers)

@app.route('/add_worker', methods = ['GET', 'POST'])
def add_worker():
    form = AddWorker()
    if form.validate_on_submit():
        w = Worker(first_name = form.first_name.data, last_name = form.last_name.data,
        position = form.position.data)
        db.session.add(w)
        db.session.commit()
        return redirect(url_for('home'))
        flash('Worker ' + w.first_name + 'was added!')
    return render_template('add_worker.html', form = form)

@app.route('/edit_worker', methods = ['GET', 'POST'])
def edit_worker():
    workers = Worker.query.all()
    return render_template('select_worker.html', workers = workers)

@app.route('/worker/<first_name>',  methods = ['GET', 'POST'])
def worker(first_name):
    worker = Worker.query.filter_by(first_name=first_name).first_or_404()
    form = AddWorker()
    if form.validate_on_submit():
        worker.first_name = form.first_name.data
        worker.last_name = form.last_name.data
        worker.position = form.position.data
        db.session.commit()
        flash('Worker info edited!')
        return redirect(url_for('home'))
    form.first_name.data= worker.first_name
    form.last_name.data = worker.last_name
    form.position.data = worker.position
    return render_template('add_worker.html', form = form, worker = worker)

@app.route('/edit_availability', methods = ['GET', 'POST'])
def edit_availability(worker):
    form = EditAvailability()
    current_availability = worker.availabilities.first()
    form.monday.data = current_availability.monday
    form.tuesday.data = current_availability.tuesday
    form.wednesday.data = current_availability.wednesday
    form.thursday.data = current_availability.thursday
    form.friday.data = current_availability.friday
    form.saturday.data = current_availability.saturday
    form.sunday.data = current_availability.sunday
    return render_template('edit_availability.html', form = form, worker = worker)

@app.route('/add_schedule', methods = ['GET', 'POST'])
def add_schedule():
    return render_template('add_schedule.html')


if "__name__" == "__main__":
    app.run(debug = True)