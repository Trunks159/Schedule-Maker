from config import db

class Worker(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.String(60), index = True)
	last_name = db.Column(db.String(60), index = True)
	position = db.Column(db.String(60), index = True)
	availabilities = db.relationship('Availability', backref='worker', lazy='dynamic')

	def __repr__(self):
		return 'Worker {}'.format(self.name)

class Availability(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	monday = db.Column(db.String(60), index = True)
	tuesday = db.Column(db.String(60), index = True)
	wednesday = db.Column(db.String(60), index = True)
	thursday = db.Column(db.String(60), index = True)
	friday = db.Column(db.String(60), index = True)
	saturday = db.Column(db.String(60), index = True)
	sunday = db.Column(db.String(60), index = True)
	user_id = db.Column(db.Integer, db.ForeignKey('worker.id'))

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

#w = Worker(name = 'Jordan Giles', position = 'manager')
#a = Availability(worker = w, tuesday = "12:00PM - 11:00PM")

#@login.user_loader
#def load_user(id):
#	return User.query.get(int(id))