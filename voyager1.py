import datetime
import ru_local as ru

SPD = 38241
DSTNC = 16637000000
RADIO_WAVE = 299792458

print(ru.DATE)

# Number of days that have passed.
delta = int(input())
date1 = datetime.date(2009, 9, 25)
# Date in n number of days.
date2 = datetime.timedelta(days=delta)

# Distance per day.
distanceday = SPD * 24
# Distance per period.
distanceperiod = distanceday * date2.days
distancesun = DSTNC + distanceperiod
# Wireless delay in hours.
delay = distancesun / (RADIO_WAVE * 3600 / 1000 / 1.609)

print(distanceday, ru.PER_DAY)
print(distanceperiod, ru.PERIOD, date2.days, ru.DAYS)
print(distancesun, ru.MILE, round(distancesun * 1.609, 2), ru.KM, round(distancesun * 1.609 / 149597870.7, 2), ru.AU)
print(ru.DELAY_HOURS, round(delay, 2))
