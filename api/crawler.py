import requests

def kaggle_crawler(username):
    url = 'https://www.kaggle.com/' + username
    resp = requests.get(url).text
    resp = resp[resp.find('ProfileContainerReact'):]
    resp = resp[resp.find('Kaggle.State.push'):]
    displayName = resp[resp.find('displayName')+14:resp.find('country')-3]
    country = city = occupation = organization = ''
    if 'country' in resp:
        country = resp[resp.find('country')+10:resp.find('city')-3]
    if 'city' in resp:
        city = resp[resp.find('city')+7:resp.find('gitHubUserName')-3]
    if 'occupation' in resp:
        occupation = resp[resp.find('occupation')+13:resp.find('organization')-3]
    if 'organization' in resp:
        organization = resp[resp.find('organization')+15:resp.find('bio')-3]
    performanceTier = 'NOVICE'
    if 'performanceTier' in resp:
        performanceTier = resp[resp.find('performanceTier')+18:resp.find('performanceTierCategory')-3]
    performanceTierCategory = resp[resp.find('performanceTierCategory')+26:resp.find('activePaneTier')-3]
    if performanceTierCategory:
        if '_' in performanceTierCategory:
            performanceTierCategory = performanceTierCategory.split('_')[-1]

    print(displayName, country, city, occupation, organization, performanceTier, performanceTierCategory)

if __name__ == '__main__':
    kaggle_crawler('simon168')