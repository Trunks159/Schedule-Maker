from config import db

class Worker(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.String(60), index = True)
	last_name = db.Column(db.String(60), index = True)
	availability = db.Column(db.String(100), index = True)
	off_days = db.Column(db.String(100), index = True)
	age = db.Column(db.Integer, index = True)
	competence = db.Column(db.String(5), index = True)
	position = db.Column(db.String(), index = True)

	def info(self):
		return [self.first_name + self.last_name, self.availability, self.off_days,
		self.age, self.competence, self.position]

	def avatar(self):
		pass 

	def __repr__(self):
		return 'Worker {}'.format(self.first_name)

#class Post(db.Model):
#	id = db.Column(db.Integer, primary_key = True)
#	body = db.Column(db.String(140))

#	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#	def __repr__(self):
#		return 'Post {}'.format(self.body)	


#@login.user_loader
#def load_user(id):
#	return User.query.get(int(id))