import datetime
import ru_local as ru

SPD = 38241
DSTNC = 16637000000
RADIO_WAVE = 299792458
print(ru.DATE)
year = int(input())
month = int(input())
day = int(input())
date1 = datetime.date(2009, 9, 25)
date2 = datetime.date(year, month, day)
delta = date2 - date1
distanceday = SPD * 24
distanceperiod = distanceday * delta.days
distancetosun = DSTNC + distanceperiod
delay = distancetosun / (RADIO_WAVE * 3600 / 1000 / 1.609)
print(delta.days, ru.DAYS)
print(distanceday, ru.PER_DAY)
print(distanceperiod, ru.PERIOD, delta.days, ru.DAYS)
print(distancetosun, ru.MILE, round(distancetosun * 1.609, 2), ru.KM, round(distancetosun * 1.609 / 149597870.7, 2), ru.AU)
print(ru.DELAY_HOURS, round(delay, 2))
