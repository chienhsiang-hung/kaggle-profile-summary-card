import requests
import base64

def img_to_datauri(img_url):
    resp = requests.get(img_url, stream=True)
    return base64.b64encode( resp.content ).decode()