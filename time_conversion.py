#convert function:
#takes list of times with each time in format:
#'Day ##:##A/PM-##:##A/PM'
# and returns a dictionary with the info in format:
#{'Day1':['time1', 'time2'],'Day2':['time1', 'time2'] }
from datetime import time, timedelta

def split_comma(x):
	comma = ','
	if comma in x: x = x.split(',')
	for i in range(len(x)): x[i] = x[i].strip()
	return x

def meridian(segment):
	if 'PM' in segment:
		old_time = segment.replace('PM', '')
		old_time = old_time.split(':')
		old_time[0]= str(int(old_time[0])+ 12)
		return old_time[0] + ':' + old_time[1]
	else:
		return segment.replace('AM', '')

def func2(x):
	x = x.split(' ')
	y = []
	day = x[0]
	time = x[1]
	time = time.split('-')
	for segment in time:
		y.append(meridian(segment))
	return [day, y]

def convert(x):
	y = {}
	strings = split_comma(x)
	if isinstance(strings, list):
		for item in strings:
			c = func2(item)
			y[c[0]] = c[1]
	else:
		c = func2(strings)
		y[c[0]] = c[1]		
	return y

def set_all():
	y = {}
	days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
	default = "7:00AM-11:00PM"
	for day in days:
		y[day] = default
	return y

#test : print(convert('Monday 3:30PM-11:00PM, Sunday 8:30AM-3:30PM'))




t = time(4,30)
x = t.hour*3600 + t.minute*60 +t.second
td = timedelta(seconds = x)
#print(td)