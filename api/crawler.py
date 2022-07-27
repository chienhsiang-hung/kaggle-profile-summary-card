import requests

def kaggle_crawler(username):
    url = 'https://www.kaggle.com/' + username
    resp = requests.get(url).text
    resp = resp[resp.find('ProfileContainerReact'):]
    resp = resp[resp.find('Kaggle.State.push'):]
    displayName = resp[resp.find('displayName')+14:resp.find('country')-3]
    country = resp[resp.find('country')+10:resp.find('city')-3]
    city = resp[resp.find('city')+7:resp.find('gitHubUserName')-3]
    print(displayName, country, city)

if __name__ == '__main__':
    kaggle_crawler('chienhsianghung')