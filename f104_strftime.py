# .strftime() string-format-time datetime => str
# .strptime() string-parse-time  str => datetime

import datetime
now = datetime.datetime.now()
print(now)
print(now.strftime('%Y -*- %m -*- %A'))
print(now.strftime('%A, %d-%m-%Y'))

s = 'Wednesday, 23-08-2017'
dt = datetime.datetime.strptime(
	s,
	'%A, %d-%m-%Y')
print(dt)
