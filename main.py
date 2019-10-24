from flask import render_template, flash, redirect, url_for, request
from config import app, migrate, db
from werkzeug.urls import url_parse
from models import Worker
from forms import AddWorker


@app.route('/')
@app.route('/home')
def home():
    workers = Worker.query.all()
    return render_template('hello.html', workers = workers)

@app.route('/add_worker', methods = ['GET', 'POST'])
def add_worker():
    form = AddWorker()
    if form.validate_on_submit():
        w = Worker(first_name = form.first_name.data, last_name = form.last_name.data,
            availability = form.availability.data, off_days = form.off_days.data,
            age = form.age.data, competence = form.competence.data, 
            position = form.position.data)
        db.session.add(w)
        db.session.commit()
        return redirect(url_for('home'))
        #flash('Congrats your registration was successful')
    return render_template('add_worker.html', form = form)

@app.route('/team')
def team():
    workers = Worker.query.all()
    return render_template('team.html', workers = workers)


if "__name__" == "__main__":
    app.run(debug = True)