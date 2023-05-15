import untangle
from datetime import date
from socket import *
import os
from http_utils import get_XML_from_URL
from geo_utils import dd2dm_raw,dmraw2aprsformat
from dotenv import load_dotenv
from aprs_utils import generate_valid_id, generate_aprs_timestamp
import time
import XmlManager

# Constants
xmlFileName = 'IncidenciasTDT.xml'

print("=================================")
print("     aprs_traffic_eus v0.0.1     ")
print("=================================")
print()

# Load environment variables
print("- Loading environment variables...")
load_dotenv()
url = os.environ.get('URL')
server = os.environ.get('APRS_SERVER_URL')
port = os.environ.get('APRS_SERVER_PORT')
callsign = os.environ.get('CALLSIGN')
password = os.environ.get('CALLSIGN_PASS')
ssid = os.environ.get('CALLSIGN_SSID')

# Get date
print("- Retrieving date...")
today_YYmmdd = date.today().strftime("%Y-%m-%d")

# Download new XML from source
print("- Retrieving XML from source...")
url = os.environ.get('URL')
get_XML_from_URL(url, xmlFileName)

# Parse XML file
print("- Parsing XML file...")
obj = untangle.parse(xmlFileName)

# Filtering incidences
print("- Filtering incidences...")
xml_manager = XmlManager.XmlManager(obj)
list_of_incidences = xml_manager.filter_incidences(today_YYmmdd)
    
print('- Total incidences in XML file: ' + str(xml_manager.get_xml_incidences()))
print('- Today incidences: ' + str(xml_manager.get_today_incidences()))
print('- Filtered incidences: ' + str(xml_manager.get_filtered_incidences()))

xml_manager.print_filtered_incidences()
print()

# APRS
first_symbol = '\\'
second_symbol = '!'

# Send all incidences
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

    