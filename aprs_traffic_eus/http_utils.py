import requests

def get_XML_from_URL(url):
    r = requests.get(url, allow_redirects=True)
    open('IncidenciasTDT.xml', 'wb').write(r.content)
    