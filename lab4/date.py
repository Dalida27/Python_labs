from datetime import datetime
import datetime

#exercise 1
todayd = datetime.date.today()
tdelta = datetime.timedelta(days=5)
print(todayd - tdelta)



#exercise 2
yday = datetime.date.today()
ydelta = datetime.timedelta(days=1)
print(yday - ydelta) #yesterday

tday = datetime.date.today()
print(tday)#today

tmday = datetime.date.today()
tmdelta = datetime.timedelta(days=1)
print(yday + tmdelta)#tomorrow



#exercise 3
dt= datetime.datetime.today()
dt1 = dt.replace(microsecond=0)
print(dt1)


#exercise 4
tday = datetime.date.today()
sday = datetime.date(2024, 6, 1)
left_days = sday - tday
print(left_days.total_seconds())
