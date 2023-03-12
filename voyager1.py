import datetime
import ru_local as ru
spd = 38241
dstnc = 16637000000
radio_wave = 299792458
print(ru.DATE)
year = int(input())
month = int(input())
day = int(input())
date1 = datetime.date(2009, 9, 25)
date2 = datetime.date(year, month, day)
delta = date2 - date1
distanceday = spd * 24
distanceperiod = distanceday * delta.days
distancetosun = dstnc - distanceperiod
delay = distancetosun / (radio_wave * 3600 / 1000 / 1.609)
print(delta.days, ru.DAYS)
print(distanceday, ru.PER_DAY)
print(distanceperiod, ru.PERIOD, delta.days, ru.DAYS)
print(distancetosun, ru.MILE, round(distancetosun * 1.609, 2), ru.KM, round(distancetosun * 1.609 / 149597870.7, 2), ru.AU)
print(ru.DELAY_HOURS, round(delay, 2))