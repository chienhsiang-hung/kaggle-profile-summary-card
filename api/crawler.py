import requests, json

def kaggle_crawler(username):
    url = 'https://www.kaggle.com/' + username
    resp = requests.get(url).text
    resp = resp[resp.find('ProfileContainerReact'):]
    resp = resp[resp.find('Kaggle.State.push'):]
    print
    push_json = resp[18: resp.find('performance &&') -2 ]
    push_json = json.loads(push_json)

    userAvatarUrl = 'https://storage.googleapis.com/kaggle-avatars/images/default-thumb.png' if 'userAvatarUrl' not in push_json else push_json['userAvatarUrl']
    displayName = push_json['displayName']
    country = push_json['country'] if 'country' in push_json else ''
    city = push_json['city'] if 'city' in push_json else ''
    occupation = push_json['occupation'] if 'occupation' in push_json else ''
    organization = push_json['organization'] if 'organization' in push_json else ''
    performanceTier = push_json['performanceTier'] if 'performanceTier' in push_json else 'NOVICE'
    performanceTierCategory = push_json['performanceTierCategory'].split('_')[-1]

    return userAvatarUrl, displayName, country, city, occupation, organization, performanceTier, performanceTierCategory

    # if 'occupation' in resp:
    #     occupation = resp[resp.find('occupation')+13:resp.find('organization')-3]
    # if 'organization' in resp:
    #     organization = resp[resp.find('organization')+15:resp.find('bio')-3]
    # performanceTier = 'NOVICE'
    # if 'performanceTier' in resp:
    #     performanceTier = resp[resp.find('performanceTier')+18:resp.find('performanceTierCategory')-3]
    # performanceTierCategory = resp[resp.find('performanceTierCategory')+26:resp.find('activePaneTier')-3]
    # if performanceTierCategory:
    #     if '_' in performanceTierCategory:
    #         performanceTierCategory = performanceTierCategory.split('_')[-1]

    # print(displayName, country, city, occupation, organization, performanceTier, performanceTierCategory)

if __name__ == '__main__':
    print( kaggle_crawler('chienhsianghung') )