import datetime

def hours_since_birth(birthdate):
	now = datetime.datetime.now()
	delta = now - birthdate
	hours = delta.days * 24
	hours = hours + (delta.seconds / (60.0 * 60.0))
	return hours

year, month, day = input('Enter birthdate (yyyy-mm-dd): ').split('-')

bd = datetime.datetime(
	year=int(year), month=int(month), day=int(day)
)
print('Hours since birth: {:.2f}'.format(hours_since_birth(bd)))





def hundredth_day_since_birth(birthdate):
	return birthdate + datetime.timedelta(days=100)

bd = datetime.date(
	year=int(year), month=int(month), day=int(day)
)
print('100th day since birth:', hundredth_day_since_birth(bd))









#
