




#dt = datetime.combine(date.today(), time(5, 44)) - datetime.combine(date.today(), time(3, 13))
#print(dt.seconds)

def to_hours(seconds):
	return seconds / 3600

#print(to_hours(dt.seconds))

print(translate_after_3('before3')[1])