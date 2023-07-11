import untangle
from datetime import date
from socket import *
import os
from http_utils import get_XML_from_URL
from geo_utils import dd2dm_raw,dmraw2aprsformat
from file_utils import normalize_characters
from aprs_utils import send_incidences
from dotenv import load_dotenv
from aprs_utils import generate_valid_id, generate_aprs_timestamp
import time
import XmlManager


# Constants
xmlFileNameIn = 'IncidenciasTDT.xml'
xmlFileNameOut = 'IncidenciasTDT_r.xml'

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
get_XML_from_URL(url, xmlFileNameIn)

# Replace non-UTF8 characters
normalize_characters(xmlFileNameIn, xmlFileNameOut)

# Parse XML file
print("- Parsing XML file...")
obj = untangle.parse(xmlFileNameOut)

# Filtering incidences
print("- Filtering incidences...")
xml_manager = XmlManager.XmlManager(obj)
list_of_incidences = xml_manager.filter_incidences(today_YYmmdd)
    
print('- Total incidences in XML file: ' + str(xml_manager.get_xml_incidences()))
print('- Today incidences: ' + str(xml_manager.get_today_incidences()))
print('- Filtered incidences: ' + str(xml_manager.get_filtered_incidences()))

xml_manager.print_filtered_incidences()
print()

# Send all incidences
send_incidences(list_of_incidences, server, port, callsign, password, ssid)
    