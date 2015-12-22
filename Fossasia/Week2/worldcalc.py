import time
import math
import ephem
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
from datetime import datetime
geolocator = Nominatim()
location1 = geolocator.geocode("1600 Amphitheatre Parkway", timeout=20)
location2 = geolocator.geocode("Singapore 139951", timeout=20)
today = datetime.today()
JDAY = int(362.25*(today.year)+4716)+int(30.6001*(today.month)+1)+today.day+(today.hour+float(today.minute/60)/24)+0-1524.5
JC = ((JDAY - 2451545)/36525)
january = datetime(2015,01,01)       
J2000 = datetime(2000,01,01) # To get the sun position we must use J2000.0
difference = (today - J2000)
daysfromj2000 = difference.days
januarydifference = (today-january).days
#J2000 is set at 12.00 TT
#Time is measured in degrees here (180 degs = 12h)
#Below is the formula to get the sun's position
longitude = (280.460 + (0.9856474 * daysfromj2000))
#Mean longitude including aberration
while longitude < 0:
	longitude += 360
while longitude > 360:
	longitude -= 360
	
anomaly = (357.528 + (0.9856003 * daysfromj2000))
#Mean anomaly
while anomaly < 0:
        anomaly += 360
while anomaly > 360:
        anomaly -=  360

ecliptic_longitude = longitude + (1.915 * math.sin(anomaly)) + (0.020 * math.sin(2*anomaly))  #Correct the eq centre
while ecliptic_longitude > 360:
	ecliptic_longitude -= 360
while ecliptic_longitude < 0:
	ecliptic_longitude +=360

obliquity = 23.4393 - (0.0000004 * daysfromj2000)
sun = ephem.Sun(today)
# Alpha = Sun's right ascension
ascension = math.degrees(float(sun.g_ra))/15 #Apparent Geocentric Position expressed in hours 
delta = math.degrees(float(sun.g_dec)) #Apparent Geocentric Position
suntoearth = 1.00014 - 0.01671*math.cos(anomaly)-0.00014*math.cos(2*anomaly) #Distance from the Earth to the Sun in astronomic units
TESTGMT =280.46061837+360.98564736629*(JDAY-2451545)+0.000387933*JC**2-((JC**3)/38710000)
TESTGMT = TESTGMT/360
if TESTGMT >= 0:
        TESTGMT = 360 * (TESTGMT % 1)
else:
        TESTGMT = 360 - (360 * (TESTGMT % 1))

#Equation of time
Eqoftime = (-7.655*math.sin(januarydifference))+(9.873*math.sin(2*januarydifference+3.588)) 
Eqoftime = ((float(Eqoftime)/60)/24)*360

LMST = TESTGMT+Eqoftime
while LMST < 0:
        LMST += 360
while LMST > 360:
        LMST -= 360

#suntransit = (ascension-local_longitude-LMST)/360
#Local hour angle formula = (Zenith - sin(latitude)*sin(delta))/cos(latitude)*cos(delta)
def sunrise(location):
        sun = ephem.Sun(today)
        # Alpha = Sun's right ascension
        ascension = math.degrees(float(sun.g_ra))/15 #Apparent Geocentric Position expr$
        delta = math.degrees(float(sun.g_dec)) #Apparent Geocentric Position
	z = math.radians(math.cos(90)) - (math.sin(math.radians(location.latitude))*math.sin(math.radians(delta)))
	b = math.cos(math.radians(location.latitude))*math.cos(math.radians(delta))
	c = math.acos(z/b)
	localhourangle = (360 - math.degrees(c))/15 
	lngHour = location.longitude / 15
	t = float(januarydifference + ((6 - lngHour) / 24))
	sunrise = localhourangle + ascension - (0.06571 * t) - 6.622 #localmeantime
        #Convert sunrise into UTC
	ut = sunrise-lngHour
	f = ((ut % 1) * 60)/100
	ut = (int(ut) + f)
	ut = ut - (ut % 0.01)
	return ut

def distance_difference(location1, location2):
	return vincenty((location1.latitude, location1.longitude), (location2.latitude, location2.longitude)).miles

def hour_difference(hour1, hour2):
	if hour1 > hour2:
		final = hour1-hour2-0.40
		if final % 1 > 0.60:
			final = final
		print "The sun rises " +str(final) + " earlier in Location2 than in Location1"
	else:
		final = hour2-hour1-0.40
		if final % 1 > 0.60:
			final = final -0.40
		print "The sun rises " +str(final)+ " later in Location2 than in Location1"
print "Welcome to the World Distance Calculator, it have been " + str(daysfromj2000) + " days since J2000.0"
print "In today's facts:"
print "Delta is " + str(delta)
print "Right ascension is " + str(ascension)
print "Sidereal time " + str(TESTGMT)
print "Local sidereal time" + str(LMST)
print "Eq of time " + str(Eqoftime)
print "-------------------------------------------------------------"
print "Take a look at some examples!"
print "Just input name of the City and Country of two different places"
print "This script will handle the rest!"
print "In Google's headquarters at Mountain View"
sunrise(location1)
print "In the current location of Fossasia 2016 Conference at Singapore"
sunrise(location2)
print "The difference of distances from this two points in miles is: "
print distance_difference(location1,location2)
location3 = raw_input("Input the address and coordinates to geolocate the query")
location3 = geolocator.geocode(location3, timeout=20)
print "In the first location the Sun rises at " + str(sunrise(location3)) + " (HOURS:MINUTES) UTC/GMT"
location4 = raw_input("Input the address and coordinates to geolocate the query")
location4 = geolocator.geocode(location4, timeout=20)
print "In the second location the Sun rises at " + str(sunrise(location4)) + " (HOURS:MINUTES) UTC/GMT"
print "The difference of distances from this two points in miles is: "
print distance_difference(location3,location4)
hour_difference(sunrise(location3), sunrise(location4))

