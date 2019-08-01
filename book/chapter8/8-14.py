def make_car(Manufacturer, model, **user_info):
    car = {'type': 'SUV', 'sent': "20W"}
    car['Manufacturer_name'] = Manufacturer
    car['Model'] = model
    for key, value in user_info.items():
        car[key] = value
    return car
    # print(car)


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
