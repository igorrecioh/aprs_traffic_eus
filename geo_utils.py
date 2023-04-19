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

    print(str(degrees_lat) + "º" + str(mins_lat) + char_lat + ", " + str(degrees_long) + "º" + str(mins_long) + char_long)


lat = 43.0167
long = -2.5412

dd2dm_raw(lat,long)