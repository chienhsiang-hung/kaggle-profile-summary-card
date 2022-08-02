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

def summary_crawler(username):
    url = 'https://www.kaggle.com/' + username
    resp = requests.get(url)

    # handle no user error
    if resp.status_code == 404:
        return False * 13

    resp = resp.text
    resp = resp[resp.find('ProfileContainerReact'):]
    resp = resp[resp.find('Kaggle.State.push'):]
    
    push_json = resp[18: resp.find('performance &&') -2 ]
    push_json = json.loads(push_json)

    userAvatarUrl = 'https://storage.googleapis.com/kaggle-avatars/images/default-thumb.png' if 'userAvatarUrl' not in push_json else push_json['userAvatarUrl']
    displayName = push_json['displayName']
    competitionsSummary_tier = push_json['competitionsSummary']['tier'] if 'tier' in push_json['competitionsSummary'] else 'NOVICE'
    scriptsSummary_tier = push_json['scriptsSummary']['tier'] if 'tier' in push_json['scriptsSummary'] else 'NOVICE'
    discussionsSummary_tier = push_json['discussionsSummary']['tier'] if 'tier' in push_json['discussionsSummary'] else 'NOVICE'
    datasetsSummary_tier = push_json['datasetsSummary']['tier'] if 'tier' in push_json['datasetsSummary'] else 'NOVICE'

    competitionsAchieveUrl, competitionscolorAchieve = userAchieveUrl_switcher.get(competitionsSummary_tier)
    scriptsSummaryAchieveUrl, scriptscolorAchieve = userAchieveUrl_switcher.get(scriptsSummary_tier)
    discussionsSummaryAchieveUrl, discussionscolorAchieve = userAchieveUrl_switcher.get(discussionsSummary_tier)
    datasetsAchieveUrl, datasetscolorAchieve = userAchieveUrl_switcher.get(datasetsSummary_tier)

    followers = push_json['followers']['count'] if 'count' in push_json['followers'] else 0
    following = push_json['following']['count'] if 'count' in push_json['following'] else 0

    userJoinDate = push_json['userJoinDate'][:10]

    return (
        userAvatarUrl, displayName,
        competitionsAchieveUrl, competitionscolorAchieve,
        scriptsSummaryAchieveUrl, scriptscolorAchieve,
        discussionsSummaryAchieveUrl, discussionscolorAchieve,
        datasetsAchieveUrl, datasetscolorAchieve,
        followers, following, userJoinDate
    )

if __name__ == '__main__':
    print( kaggle_crawler('chienhsianghung') )
    print( summary_crawler('chienhsianghung') )
    print( summary_crawler('chienhsianghun') )