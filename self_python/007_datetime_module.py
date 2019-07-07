# Datetime Module
# https://docs.python.org/3/library/datetime.html
import datetime
import pytz

# help(pytz.timezone)

"""
See all the time zone

for tz in pytz.all_timezones:
    print tz
"""

# Naive : y, m, d
# d = datetime.date(2001, 9, 11) # Do NOT PASS IN 09 instead of 9.

tday = datetime.date.today()
# print(tday.year)# print out year
# print(tday.day)

# weekday() # - Monday is 0 and Sunday is 6
# print(tday)
# print(tday.weekday())


# isoweekday() - Monday is 1 and Sunday is 7
# print(tday.isoweekday())


# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
tdelta = datetime.timedelta(days=7)  # what the date will be one week (7 days) from now

# tdelta = datetime.timedelta(hours=12)

# print(tday + tdelta) # 7 days from now
# print(tday - tdelta) # 7 days ago


# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2020, 3, 25)

till_bday = bday - tday  # -103 days: my birthday already happened 103 days ago in 2019

print(till_bday.days)  # 263 days till my next my birthday in 2020
print(till_bday.total_seconds())


# NOW lets look at the datetime.time() >>>>>>>  h:m:s:ms
t = datetime.time(9, 30, 45, 100000)

# dt = datetime.datetime.today()
# dtnow = datetime.datetime.now()
# print(dir(datetime.datetime))
# print(dt)
# print(dtnow)


# datetime.datetime >>>>>>>> gives both date and time
dt = datetime.datetime(2019, 7, 24, 12, 30, 45, tzinfo=pytz.UTC)
# print(dir(dt))
# print(dt) # 2019-07-24 12:30:45+00:00
# print(dt.date())
# print(dt.time())
# print(dt.year)

# datetime.timedelta: >>>>>>>

tdelta = datetime.timedelta(days=7)
# print(dt + tdelta) # 1 week from now
# print(dt + datetime.timedelta(hours=12)) # 12 hours from now

dt_now = datetime.datetime.now()
dt_today = datetime.datetime.today()
dt_utcnow = datetime.datetime.utcnow()

print(dt_now)  # 2019-07-06 12:54:44.067724 : not time zone aware
# print(dt_today)
# print(dt_utcnow)


# time zone: PREFERRED
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)  # 2019-07-06 16:46:47.801247+00:00


dt_utcnow2 = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow2)

# dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
# print(dt_mtn)
# Canada estern time
# >> PREFERED
dt_mtn = datetime.datetime.now()
mtn_tz = pytz.timezone('Canada/Eastern')
dt_mtn = mtn_tz.localize(dt_mtn)
# print(mtn_tz)
print(dt_mtn)  # 2019-07-06 12:56:12.611519-04:00


dt_east = dt_mtn.astimezone(pytz.timezone('Canada/Eastern'))
# print(dt_east) # 2019-07-06 12:56:12.611519-04:00


# FORMAT >>>>>>>>>>>>>>

# convert datetime to a string
print(dt_mtn)
print(dt_mtn.strftime('%B %d, %Y'))

# convert a string to a datetime format
dt_str = 'July 6, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# strftime - Datetime to String
# strptime - String to Datetime

# Notes: there is another package called arrow to work with datetime
