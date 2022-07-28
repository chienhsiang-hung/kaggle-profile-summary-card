import requests, json

def kaggle_crawler():
    url = 'https://www.kaggle.com/chienhsianghun'
    resp = requests.get(url)
    return resp

if __name__ == '__main__':
    print(kaggle_crawler().status_code == 404)