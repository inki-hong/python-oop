import datetime

print(dir(datetime))
print('-' * 40)

my_dir = [s for s in dir(datetime)
          if not s.startswith('__')]
print(my_dir)
print('-' * 40)
print('\n'.join(my_dir))
print('-' * 40)

print(datetime.date)
print(datetime.time)
print(datetime.datetime)
print(datetime.timezone)
print(datetime.timedelta)
print('-' * 40)


d1 = datetime.date(2017, 8, 16)
print(d1, type(d1))

d2 = datetime.date(month=8, day=16, year=2017)
print(d2, d1 == d2)

d3 = datetime.date.today()
print(d3)
print(d3.year)
print(d3.month)
print(d3.day)
print(d3.weekday())

print(d3.strftime('%Y -*- %m -*- %d (%A)'))
print('-' * 40)



t1 = datetime.time(10, 30, 20)  # 24-hour clock
print(t1, type(t1))

t2 = datetime.time(second=20, minute=30, hour=10)
print(t2, t1 == t2)

t3 = datetime.time(hour=10, minute=30, second=20,
	               microsecond=5000)
print(t3)

print(t3 > t2)

print('-' * 40)





dt1 = datetime.datetime(
    year=2017, month=8, day=16,
    hour=10, minute=30, second=20,
    microsecond=5000
)
print(dt1)
print(dt1.year)
print(dt1.hour)

now = datetime.datetime.now()
print(now, now > dt1)

print('-' * 40)





td = datetime.timedelta(hours=9)
tz = datetime.timezone(td)
t4 = datetime.time(hour=10,
	               minute=30,
	               second=20,
	               tzinfo=tz)
print(t4)

print('-' * 40)















today = datetime.date.today()
dt2 = datetime.datetime(year=today.year,
	                    month=today.month,
	                    day=today.day,
	                    hour=10,
	                    minute=30,
	                    second=20,
	                    tzinfo=tz)
print(dt2)
print('-' * 40)








dt3 = datetime.datetime.now(tz=tz)  # "tz" instead of "tzinfo"
print(dt3)

print('dt3 is {} dt2'.format(
        'after' if dt3 > dt2 else 'before'
))

print('-' * 40)
########################################









tz1 = datetime.timezone(datetime.timedelta(hours=9))
tz2 = datetime.timezone(offset=datetime.timedelta(hours=-5))
print(tz1, tz2)

print('-' * 40)
########################################












td1 = datetime.timedelta(weeks=5)
td2 = datetime.timedelta(days=5)
td3 = datetime.timedelta(hours=9)
td4 = datetime.timedelta(minutes=30)
td5 = datetime.timedelta(seconds=15)
td6 = datetime.timedelta(milliseconds=150)
td7 = datetime.timedelta(microseconds=200)
print(td1.days, td2.days)
print(td3.seconds, td5.seconds)
print(td7.microseconds)
print('-' * 40)

td8 = datetime.timedelta(weeks=1, days=2)
print(td8.days)

td9 = datetime.timedelta(days=2, hours=2)
print(td9.days, td9.seconds)
