import requests, json

userAchieveUrl_switcher = {
    'NOVICE': ['https://www.kaggle.com/static/images/tiers/novice@96.png', '#5ac995'],
    'CONTRIBUTOR': ['https://www.kaggle.com/static/images/tiers/contributor@96.png', '#0bf'],
    'EXPERT': ['https://www.kaggle.com/static/images/tiers/expert@96.png', '#95628f'],
    'MASTER': ['https://www.kaggle.com/static/images/tiers/master@96.png', '#f96517'],
    'GRANDMASTER': ['https://www.kaggle.com/static/images/tiers/grandmaster@96.png', '#dca917']
}

def kaggle_crawler(username):
    url = 'https://www.kaggle.com/' + username
    resp = requests.get(url)

    # handle no user error
    if resp.status_code == 404:
        return None, None, None, None, None, None, None, None, None, None, False
    
    resp = resp.text
    # test
    with open(f'test/crawler/{username}_resp.txt', 'w') as f:
        f.write(resp)
    resp = resp[resp.find('ProfileContainerReact'):]
    resp = resp[resp.find('Kaggle.State.push'):]
    
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
    userJoinDate = push_json['userJoinDate'][:10]

    userAchieveUrl = userAchieveUrl_switcher.get(performanceTier)[0]
    colorAchieve = userAchieveUrl_switcher.get(performanceTier)[1]

    return userAvatarUrl, displayName, country, city, occupation, organization, performanceTier.capitalize(), performanceTierCategory.capitalize(), userJoinDate, userAchieveUrl, colorAchieve


if __name__ == '__main__':
    print( kaggle_crawler('chienhsianghung') )
    print( kaggle_crawler('simon168') )