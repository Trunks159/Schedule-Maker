from config import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from config import login
from datetime import date, datetime, timedelta



class Worker(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.String(20), index = True)
	last_name = db.Column(db.String(20), index = True)
	level = db.Column(db.Integer, index = True)
	availability = db.relationship('Day', backref='worker', lazy='dynamic')
	user = db.relationship('User', backref='worker', lazy='dynamic')

	def __repr__(self):
		return 'Worker {}'.format(self.first_name)

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(64), index = True, unique = True)
	password_hash = db.Column(db.String(128))
	worker_id = db.Column(db.Integer, db.ForeignKey('worker.id'))

	def __repr__(self):
		return 'User {}'.format(self.username)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def avatar(self):
		return 'static/images/Skull Icon.png'


class Day(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	weekday = db.Column(db.Integer, index = True)
	day = db.Column(db.Integer)
	month = db.Column(db.Integer)
	year = db.Column(db.Integer)
	worker_id = db.Column(db.Integer, db.ForeignKey('worker.id'))
	start_time = db.Column(db.Integer)
	end_time = db.Column(db.Integer)
	available = db.Column(db.Boolean)

	def __init__(self, **kwargs):
		super(Day, self).__init__(**kwargs)
		if self.available == None: self.available = True
		self.set_available(self.available)

	def set_available(self, x):
		if x: 
			self.start_time = 700
			self.end_time = 2300
		else:
			self.start_time = None
			self.end_time = None

	def __repr__(self):
		return 'Day {}'.format(self.weekday)


'''
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
'''
'''
class Schedule(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	days = db.relationship('Day', backref= 'week', lazy = 'dynamic')
	def __init__(self, **kwargs):
		super(Schedule, self).__init__(**kwargs)

class Day(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	week_id = db.Column(db.Integer, db.ForeignKey('schedule.id'))
	date = db.Column(db.String(10), index = True, unique = True)

	def function(self):
		x = self.date.split('/')
		d = date(int(x[2]), int(x[0]), int(x[1]))
		print(d.weekday())


def convert_to_date(x):
	x = [int(item) for item in x.split('/')]
	if len(x) == 2:
		return date(datetime.now().year, x[0], x[1])
	return date(x[2], x[0], x[1])

def find_monday(x):
	return x - timedelta(days = x.weekday())

def make_week(day):
	monday = find_monday(day)
	return [monday + timedelta(days = i) for i in range(7)]

'''
@login.user_loader
def load_user(id):
	return User.query.get(int(id))