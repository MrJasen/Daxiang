# def city_country(city,country):
#     citya={'city':city,'country':country}
#     return  citya.title()
# test=city_country('santiageo','chile')
# print(test)

def city_country(city,country):
    all=city+','+country
    return  all.title()
test = city_country('santiageo','chile')
print('"'+test+'"')
test2=city_country('beijing','china')
print(test2)
test3=city_country('shanghai','china')
print(test3)