import datetime

def hours_since_birth(birthdate):
	now = datetime.datetime.now()
	delta = now - birthdate
	hours = delta.days * 24
	hours = hours + (delta.seconds / (60.0 * 60.0))
	return hours

bd = datetime.datetime(year=1982, month=10, day=10, hour=4)
print(hours_since_birth(bd))

def hundredth_day_since_birth(birthdate):
	return birthdate + datetime.timedelta(days=100)

bd = datetime.date(year=1982, month=10, day=10)
print(hundredth_day_since_birth(bd))
