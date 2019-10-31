	competence = db.Column(db.String(5), index = True)
	position = db.Column(db.String(), index = True)
		age = db.Column(db.Integer, index = True)

	def process_availability(self, old_availability):
		#takes availability typed by user and tyranslates that to a dictionary
		a = self._divide(old_availability.lower())
		days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday'
		, 'saturday', 'sunday']
		new_availability = {}
		for day in days:
			for item in a:
				if day in item:
					new_availability[day] = item.replace(day + '=', "")
				else:
					new_availability[day] = True
		return new_availability


	def set_availabilty(self, availability):
		self.availability = self.process_availability(availability)


	def time_trimmer(time):
		time = time.lower()
		letters = ['am', 'pm', ':']
		for element in time: 
			for letter in letters:
				if element is letter:
					time -= element
		time.replace()
		return time

	def _divide(self, text):
		return text.replace('"', "").replace(' ', "").split(',')

	def avatar(self):
				
