import datetime as dt

# print max year 
print(dt.MAXYEAR)

#print min year 
print(dt.MINYEAR)

# Sub module - date
dates = dt.date(2021,8,18)
# input format - YYYY,MM,DD
# ctime
print(dates.ctime())

# printing day month and year 
# day 
print(dates.day)
# month
print(dates.month)
# year
print(dates.year)

# fromisocalendar , 
print(dt.date.fromisocalendar(2021,52,4).ctime())
# parameter - year,week,day

# fromisoformat
print(dt.date.fromisoformat('2021-12-31').ctime())
# parameter - year,month,day , it should be string

# fromordinal
# it followes the georgian calender format
print(dt.date.fromordinal(235).ctime())
# parameter - georgian days

# fromtimestamp 
print(dt.date.fromtimestamp(1326244364))

# isocalendar 
print(dt.date(2021,12,31).isocalendar())

# isoformat 
print(dt.date(2021,12,31).isoformat())

# isoweekday
print(dt.date(2021,12,31).isoweekday())

# replace 
print(dt.date(2101,2,8).replace(year=2021))

# resolution 
# find the minimum unit of timedelta 
print(dt.date(2021,6,21).strftime('%d-%B-%Y'))

# represent time into a tuple format 
print(dt.date(2021,6,21).timetuple())

# toordinal 
print(dt.date(2021,5,6).toordinal())

# weekday example 
print(dt.date(2021,8,9).weekday())
print(dt.date(2021,11,11).isoweekday())

##############################################################################

# datetime 

# astimezone





# combine 
# combine both date and time 
d = dt.date(2021,2,2)
t = dt.time(12,20)
print(dt.datetime.combine(d,t))

# tzinfo - 
custom_tz = dt.timedelta(hours=7)
tzobj = dt.timezone(custom_tz,name='CSTZ')
dates_now = dt.datetime(2021,9,9,11,5,6,9,tzobj)
print(dates_now)
print(dates_now.timetz().tzinfo)
# this will show the tzinfo - timezone info
# Show the full timezone information 
print(dates_now.timetz())

# Singapore Time

sgtTimeDelta = dt.timedelta(hours=8)

sgtTZObject = dt.timezone(sgtTimeDelta, name="SGT")

dateTimeInstance = dt.datetime(2017,2,14,12,15,1,99,sgtTZObject)

print("Singapore Time instance:{}".format(dateTimeInstance))

print("UTC Offset for Singapore Time:{}".format(dateTimeInstance.utcoffset()))
