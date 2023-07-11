import time
from geo_utils import dd2dm_raw,dmraw2aprsformat
from socket import *

# APRS
first_symbol = '\\'
second_symbol = '!'

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

def send_incidences(list_of_incidences, server, port, callsign, password, ssid):
    for incidencia in list_of_incidences:
        incidence_id = generate_valid_id(incidencia.fechahora_ini)
        timestamp = generate_aprs_timestamp(incidencia.fechahora_ini)
        info = incidencia.info_msg()

        lat, long = dd2dm_raw(incidencia.latitud, incidencia.longitud)
        lat_aprs, long_aprs = dmraw2aprsformat(lat, long)

        # Create and connect to socket
        print("- Creating and connecting to socket...")
        aprsfi_socket = socket(AF_INET, SOCK_STREAM)
        aprsfi_socket.connect((str(server), int(port)))

        # Login into APRS.FI
        print("- Login into APRS.IS network")
        loginpacket = f'user {callsign} pass {password} \n'
        aprsfi_socket.send(bytes(loginpacket, 'utf-8'))
        
        # Send packet
        infopacket = f'{callsign}{ssid}>APRS,TCPIP*:;{incidence_id}*{timestamp}{lat_aprs}{first_symbol}{long_aprs}{second_symbol}{info}\n'
        print("- Sending packet: " + infopacket)
        aprsfi_socket.send(bytes(infopacket, 'utf-8'))
        
        # Close socket
        aprsfi_socket.shutdown(0)
        aprsfi_socket.close()
        time.sleep(5)

# Examples
# print(generate_valid_id("2023-04-23 21:25:35"))
# print(generate_aprs_timestamp("2023-04-23 21:25:35"))