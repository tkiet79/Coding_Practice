import calendar
month, day, year = map(int, input().split())
weekday_number = calendar.weekday(year, month, day)
day_name = calendar.day_name[weekday_number]
print(day_name.upper())