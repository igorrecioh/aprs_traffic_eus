import requests

def get_file_from_URL(url, fileName):
    r = requests.get(url, allow_redirects=True)
    open(fileName, 'wb').write(r.content)