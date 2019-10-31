from calendar import monthcalendar
from datetime import date
from models import Worker



class Schedule():
	def __init__(self):
		self.workers = 

class Request_Off():
	def __init__(self, worker, day):
		self.worker = worker
		self.day = day

class Month():
	def __init__(self, year, month):
		self.month = monthcalendar(year,month)
		self.x = []
		for week in self.month:
			for day in week:
				self.x.append(day)
		self.days = []
		for item in self.x:
			if item != 0:
				self.days.append(Day(date(year, month, item)))

	def request_off(self, request):
	 	for day in self.days:
	 		if day.date.day == request.day:
	 			day.off_days[request.worker.first_name] = day

		
class Day(object):
	def __init__(self, date):
		self.date = date
		self.off_days = {}

w = Worker(first_name = "JHope")
m = Month(2019, 11)
m.request_off(Request_Off(w, 22))
print(m.days[21].off_days)