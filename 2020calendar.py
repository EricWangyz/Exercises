import calendar
from datetime import date

myDate = date.today()
yearCalendarStr = calendar.calendar(2020)

print(f'{myDate.year}年的日历图：{yearCalendarStr}\n')
