def describe_city(city,country='美国'):
    countrys=['aaa','bbb','ccc','ddd','eee']
    if city in countrys:
        print(city+' is in  '+country)
    else:
        print(city+' not in '+country)
    #print(city+' is in  '+country)
describe_city('Reykjavik')
describe_city('aaa')
describe_city('bbb')