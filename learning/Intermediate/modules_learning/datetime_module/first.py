from datetime import date, time, datetime, timedelta

# print(type(date)) # <class 'type'>

my_date = date(2026, 8, 31)
print(my_date.day)
print(my_date.year)

print(my_date.isocalendar())

my_time = time(16, 20, 42)
print(my_time)
print(my_time.minute)

my_datetime = datetime(2222, 12, 10, 15, 10, 51)
print(my_datetime)
print(my_datetime.year)
print(my_datetime.isoformat())

print(my_datetime.now())  # Returns current datetime

print(my_datetime.strftime('%d/%b/%Y'))
print(my_datetime.strftime('%d.%m.%Y %H:%M:%S'))

date_str = '11/8/2026'

converted_date = datetime.strptime(date_str, '%d/%m/%Y')
print(converted_date)

print(timedelta)  # <class 'datetime.timedelta'>

print(my_datetime + timedelta(days=100, hours=2))
print(my_datetime - timedelta(hours=20, y))
