import math

def dd2dm_raw(latitude, longitude):
    print("Converting from DD to DM: " + str(latitude) + ", " + str(longitude))

    degrees_lat = 0
    degrees_long = 0

    mins_lat = 0.0
    mins_long = 0.0

    char_lat = ''
    char_long = ''

    frac_lat, int_lat = math.modf(lat)
    frac_long, int_long = math.modf(long)

    # Directions
    if int(int_lat) < 0:
        degrees_lat = abs(int(int_lat))
        char_lat = 'S'
    else:
        degrees_lat = int(int_lat)
        char_lat = 'N'

    if int(int_long) < 0:
        degrees_long = abs(int(int_long))
        char_long = 'W'
    else:
        degrees_long = int(int_long)
        char_long = 'E'

    # Decimal part x 60
    mins_lat = frac_lat * 60
    mins_long = abs(frac_long) * 60

    # Round to 3 decimals
    mins_lat = round(mins_lat,3)
    mins_long = round(mins_long,3)

    lat_dm_str = str(degrees_lat) + "º" + str(mins_lat) + char_lat
    long_dm_str = str(degrees_long) + "º" + str(mins_long) + char_long
    return lat_dm_str, long_dm_str

def dmraw2aprsformat(lat, long):
    print("Converting from DM to APRS format: " + str(lat) + ", " + str(long))

    # Latitude parsing
    lat_deg = lat.split('º')[0]

    lat_dec = lat.split('º')[1].split('.')[0]
    #print(lat_dec)
    if int(lat_dec) < 10:
        lat_min_str = '0' + lat_dec
    else:
        lat_min_str = lat_dec

    lat_min_dec = lat.split('º')[1].split('.')[1]
    lat_aprs_str = lat_deg + lat_min_str + "." + lat_min_dec[0] + lat_min_dec[1] + lat_min_dec[3]

    # Longitude parsing
    long_deg = long.split('º')[0]

    if int(long_deg) < 10:
        long_deg_str = '00' + long_deg
    elif int(long_deg) < 100:
        long_deg_str = '0' + long_deg
    else:
        long_deg_str = long_deg

    long_dec = long.split('º')[1].split('.')[0]
    long_min_dec = long.split('º')[1].split('.')[1]
    long_aprs_str = long_deg_str + long_dec + "." + long_min_dec[0] + long_min_dec[1] + long_min_dec[3] 

    return lat_aprs_str, long_aprs_str




lat = 43.0167
long = -2.5412
#Latitude = '4301.00N'
#Longitude = '00232.47W'
lat_dm, long_dm = dd2dm_raw(lat,long)
print(lat_dm)
print(long_dm)

lat_aprs, long_aprs = dmraw2aprsformat(lat_dm, long_dm)
print(lat_aprs)
print(long_aprs)