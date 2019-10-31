from datetime import datetime
from calendar import monthcalendar
#dt = datetime.combine(date.today(), time(5, 44)) - datetime.combine(date.today(), time(3, 13))
#print(dt.seconds)

def to_hours(seconds):
	return seconds / 3600

#print(to_hours(dt.seconds))


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

#w = Worker.query.all()
#for worker in w:
#	worker.availability = worker.process_availability(worker.availability)
#	print(worker.availability)
#	db.session.commit()

	#def translate_after_3(self, after3):
	#	end = 23
	#	start = 7 
	#	word = ''
	#	num = ''
	#	numbers = ['1','2','3','4','5','6','7','8','9','10','11','12']
	#	for char in after3:
	#		if char in numbers:
	#			num = int(char)
	#			word = after3.replace('3',"")
	#			break
	#	if num >= 3 and num <=6:
			#num += 12
		#if word == 'after':
		#	return [num, end]
		#elif word == 'before':
		#	return [start, num]

d = datetime(1899,8 , 22, 1,1, 0, 0)
print(monthcalendar(2019, 11))