import datetime

thirtyYears = datetime.timedelta(days=365 * 30)
print(datetime.datetime.now())
print(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S'))

startDate = datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')
print(startDate - thirtyYears)
