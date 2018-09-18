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

# using zip - returns an iterator of tuples
keys = ['one', 'two', 'three', 'four']
vals = ['1', '2', '3', '4']
nums_dict = dict(zip(keys, vals))
print(nums_dict)

# repeat values
print('ha' * 4)

# swap reference
a = 1; b = 2
a, b = b, a
print('a = {}, b = {}'.format(a, b))

# set values from numeric range and unpacking to a wildcard
zero, one, *two = range(4)
print('zero = {}, one = {}, two = {}'.format(zero, one, two))

# removing items by position
cheese = ['cheddar', 'stilton', 'blue cheese']
popped_cheese = cheese.pop(1)
print('popped cheese : {}, cheese : {}'.format(popped_cheese, cheese))

# removing list items by content
cheese = ['cheddar', 'stilton', 'blue cheese']
cheese.remove('stilton')
print(cheese)

# sorting using key
nums = ['323', '43', '46', '100', '4', '20']
sorted_nums = sorted(nums, key=int)
print(sorted_nums)
