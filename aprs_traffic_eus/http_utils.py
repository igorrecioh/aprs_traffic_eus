import requests

def get_XML_from_URL(url, fileName):
    r = requests.get(url, allow_redirects=True)
    open(fileName, 'wb').write(r.content)
    