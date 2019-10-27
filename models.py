from config import db
from datetime import date, datetime, time, timedelta



class Worker(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.String(60), index = True)
	last_name = db.Column(db.String(60), index = True)
	availability = db.Column(db.String(100), index = True)
	off_days = db.Column(db.String(100), index = True)
	age = db.Column(db.Integer, index = True)
	competence = db.Column(db.String(5), index = True)
	position = db.Column(db.String(), index = True)
	a = ""

	def info(self):
		return [self.first_name + self.last_name, self.availability, self.off_days,
		self.age, self.competence, self.position]

	def process_availability(self, old_availability):
		#takes availability typed by user and tyranslates that to a dictionary
		a = self._divide(old_availability.lower())
		days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday'
		, 'saturday', 'sunday']
		new_availability = {}
		for day in days:
			for item in a:
				if day in item:
					new_availability[day] = self.translate_after_3(item.replace(day + '=', ""))
				else:
					new_availability[day] = True
		return new_availability

	def time_trimmer(time):
		time = time.lower()
		letters = ['am', 'pm', ':']
		for element in time: 
			for letter in letters:
				if element is letter:
					time -= element
		time.replace()
		return time

	def translate_after_3(self, after3):
		end = 23
		start = 7 
		word = ''
		num = ''
		numbers = ['1','2','3','4','5','6','7','8','9','10','11','12']
		for char in after3:
			if char in numbers:
				num = int(char)
				word = after3.replace('3',"")
				break
		if num >= 3 and num <=6:
			num += 12
		if word == 'after':
			return [num, end]
		elif word == 'before':
			return [start, num]

	def _divide(self, text):
		return text.replace('"', "").replace(' ', "").split(',')

	def avatar(self):
		pass 

	def __repr__(self):
		return 'Worker {}'.format(self.first_name)

def time_splicer(time):
	numbers = ['1','2','3','4','5','6','7','8','9','10','11','12']
	i = 0
	for letter in time:
		if letter in numbers:
			number = letter
			break
		i+=1
	time = time.split(number)

def time_converter(time):
	time = time.lower()
	suffix = time[len(time)-2:]
	if suffix == 'am':
		time = time.replace(':',"").replace('am',"")
		c = 1 if len(time)==3 else 2
		a = int(time[:c]) * 100
		b = int(time[1:]) * 5/3
	else:
		time = time.replace(':',"").replace('pm',"")
		c = 1 if len(time)==3 else 2
		a = int(time[:c]) * 100 + 1200
		b = int(time[1:]) * 5/3
	return a + int(b)

w = Worker.query.all()
for worker in w:
	worker.availability = worker.process_availability(worker.availability)
	print(worker.availability)
#	db.session.commit()

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