import untangle
from tabulate import tabulate
from datetime import date
from socket import *
import os
from http_utils import get_XML_from_URL
from geo_utils import dd2dm_raw,dmraw2aprsformat
from dotenv import load_dotenv
from aprs_utils import generate_valid_id, generate_aprs_timestamp
import Incidence
import time

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
get_XML_from_URL(url)

# Parse XML file
print("- Parsing XML file...")
obj = untangle.parse('IncidenciasTDT.xml')


# Filtering incidences
print("- Filtering incidences...")
count_xml = 0
count_today = 0
count_filtered = 0
data_tobe_printed = []
list_of_incidences = []
for incidencia in obj.raiz.children:
    if today_YYmmdd in incidencia.fechahora_ini.cdata:
        if "Desconocida" != incidencia.causa.cdata:
            ind = Incidence.Incidence()
            prov_data = []
            ind.fechahora_ini = incidencia.fechahora_ini.cdata
            ind.tipo = incidencia.tipo.cdata
            ind.causa = incidencia.causa.cdata
            ind.carretera = incidencia.carretera.cdata
            ind.longitud = incidencia.longitud.cdata
            ind.latitud = incidencia.latitud.cdata
            ind.sentido = incidencia.sentido.cdata
            prov_data.append(incidencia.fechahora_ini.cdata)
            prov_data.append(incidencia.tipo.cdata)
            prov_data.append(incidencia.causa.cdata)
            prov_data.append(incidencia.carretera.cdata)
            prov_data.append(incidencia.longitud.cdata)
            prov_data.append(incidencia.latitud.cdata)
            prov_data.append(incidencia.sentido.cdata)
            data_tobe_printed.append(prov_data)
            list_of_incidences.append(ind)
            count_filtered+=1
        count_today+=1
    count_xml+=1
    
print('- Total incidences in XML file: ' + str(count_xml))
print('- Today incidences: ' + str(count_today))
print('- Filtered incidences: ' + str(count_filtered))

print(
    tabulate(
    data_tobe_printed, 
    headers=["Fecha/hora", "Tipo", "Causa", "Carretera", "Longitud", "Latitud", "Sentido"]
    )
    )

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

    