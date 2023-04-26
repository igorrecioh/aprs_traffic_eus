def parse_time(timestamp):
    time = timestamp.split(' ')[1]
    hour = time.split(':')[0]
    min = time.split(':')[1]
    sec = time.split(':')[2]
    return hour, min, sec

def generate_valid_id(timestamp):
    hour, min, sec = parse_time(timestamp)
    return "EUS" + str(hour) + str(min) + str(sec)

def generate_aprs_timestamp(timestamp):
    hour, min, sec = parse_time(timestamp)
    return str(hour) + str(min) + str(sec) + "/"

# Examples
# print(generate_valid_id("2023-04-23 21:25:35"))
# print(generate_aprs_timestamp("2023-04-23 21:25:35"))