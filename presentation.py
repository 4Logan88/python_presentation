# Builtin functions such as print, len, str, list, set doesn't need to be imported

a = 5
b = 10
print(a + b)
print(type(a))

# Python variables are untyped until assigned
a = 'Hello'
b = 'World'
print(a+b)
print(a, b)
print(type(a))

# Python list
cars = ['audi', 'bmw', ['honda','merc'], 'vw']
print('first element of cars is: {}'.format(cars[0]))
print('last element of cars is: {}'.format(cars[-1]))
print('cars[2][1]: {}'.format(cars[2][1]))
cars[3] = 'toyota'
print('full list of cars: {}'.format(cars))
cars.append('vw')
print('append vw to cars: {}'.format(cars))

# tuples are immutable
cars = ('audi', 'bmw', ('honda','merc'), 'vw')
# cars[3] = 'toyota'

# dictionaries
currencies_dict = {'uk':'sterling', 'us':'dollar'}
currencies_dict['germany'] = 'euro'
print('currencies dictionary = {}'.format(currencies_dict))
languages_dict = dict(uk='english', france='french')
print('language dictionary = {}'.format(languages_dict))


