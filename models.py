from config import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from config import login
from datetime import date, timedelta


def get_monday(day):
	while day.weekday() > 0: day -= timedelta(1)
	return day

def create_days(day):
	day = day.split('/')
	d = date(int(day[2]), int(day[0]), int(day[1]))
	day = get_monday(d)
	days = []
	for i in range(7):
		days.insert((day + timedelta(i)).weekday(), day + timedelta(i))
	return days


class Worker(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.String(60), index = True)
	last_name = db.Column(db.String(60), index = True)
	position = db.Column(db.String(60), index = True)
	availabilities = db.relationship('Availability', backref='worker', lazy='dynamic')
	user = db.relationship('User', backref='worker', lazy='dynamic')

	def __repr__(self):
		return 'Worker {}'.format(self.first_name)

class Availability(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	monday = db.Column(db.String(60), index = True)
	tuesday = db.Column(db.String(60), index = True)
	wednesday = db.Column(db.String(60), index = True)
	thursday = db.Column(db.String(60), index = True)
	friday = db.Column(db.String(60), index = True)
	saturday = db.Column(db.String(60), index = True)
	sunday = db.Column(db.String(60), index = True)
	worker_id = db.Column(db.Integer, db.ForeignKey('worker.id'))

	def __init__(self, **kwargs):
		super(Availability, self).__init__(**kwargs)
		self.set_defaults()

	def __repr__(self):
		return 'Post {}'.format(self.monday)

	def set_defaults(self):
		days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
		attributes = Availability.__dict__.keys()
		for attribute in attributes:
			if attribute in days and getattr(self, attribute) == None:
				setattr(self, attribute, "7:00AM-11:00PM")

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(64), index = True, unique = True)
	password_hash = db.Column(db.String(128))
	worker_id = db.Column(db.Integer, db.ForeignKey('worker.id'))

	def __repr__(self):
		return 'User {}'.format(self.username)

	def is_sm(self):
		return self.worker.position.lower() == 'sm'
	def is_gm(self):
		return self.worker.position.lower() == 'gm'
	def is_manager(self):
		return self.is_gm() or self.is_sm() 

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def avatar(self):
		return 'static/images/Skull Icon.png'


class Schedule(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	monday = db.Column(db.String(60), index = True)
	tuesday = db.Column(db.String(60), index = True)
	wednesday = db.Column(db.String(60), index = True)
	thursday = db.Column(db.String(60), index = True)
	friday = db.Column(db.String(60), index = True)
	saturday = db.Column(db.String(60), index = True)
	sunday = db.Column(db.String(60), index = True)

class Day(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	date = db.Column(db.String(10), index = True, unique = True)

	def function(self):
		x = self.date.split('/')
		d = date(int(x[2]), int(x[0]), int(x[1]))
		print(d.weekday())



#w = Worker(first_name ='Jordan', last_name = 'Giles', position = 'gm')
#u = User(username = 'Trunks159', worker = w)
#u.set_password('Trunks2296')
#db.session.add(w)
#db.session.add(u)
#print(User.query.first().worker.position)
#db.session.commit()

@login.user_loader
def load_user(id):
	return User.query.get(int(id))
