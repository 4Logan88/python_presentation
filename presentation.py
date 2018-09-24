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

# remove duplicates and items from list using set
alphabet = ['a', 'b', 'c', 'd', 'b']
removed = list(set(alphabet) - {'c'})
print(removed)

# more on sets
a1 = {1, 5, 8, 7, 6, 1}
a2 = {3, 6, 1, 4}
print('each item that is in both sets: {}'.format(a1 & a2))
print('all items in both sets: {}'.format(a1 | a2))
print('items in a1 not in a2: {}'.format(a1 - a2))
print('items that occur in one set only: {}'.format(a1 ^ a2))

# using regex with groups
import re
my_life = 'I love to take a long nap over the weekend'
m = re.search(r'(long|short).*(weekend|weekday)', my_life)
print(m.groups())

address = 'Whittington House, 19-30 Alfred Place, London. WC1E 7EA'
postcode = re.search(r'([A-Z]{2}[0-9][A-Z]?[ ][0-9][A-Z]{2})', address)
print('postcode : {}'.format(postcode.groups()[0]))

# using regex with sub
import re
address = 'Whittington House, 19-30 Alfred Place, London. WC1E 7EA'
change_postcode = re.sub(r'[A-Z]{2}[0-9][A-Z]?[ ][0-9][A-Z]{2}', 'HA7 4JA', address)
print(change_postcode)

# read the entire file into a temporary list in-memory and then iterate through that
file = open('country.txt').readlines()
for line in file:
    print(line)

# use the file object iterator
for line in open('country.txt'):
    print(line)

# function with default
def myfunc(file, dir, user='root'):
    print('{}/{}/{}'.format(file,dir,user))

myfunc('one','two')

# local variable
result = 2
def test1():
    result = 5
test1()
print(result)

# global variable
result = 2
def test2():
    global result
    result = 10
test2()
print(result)

# simple lambda
def sum(x, y):
    return (x+y)
print(sum(3, 4))

sum = lambda x,y: x+y
print(sum(3, 4))

# use filter and lambda to get even number
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0), my_list))
print(new_list)

# list comprehensions
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = [x**2 for x in range(10)]
print(squares)

# deepcopy
fruit = ['apple', 'banana', 'pear', 'orange']
lunch = fruit
fruit[1] = 'grape'
print('fruit: {}, lunch: {}'.format(fruit, lunch))

import copy
fruit = ['apple', 'banana', 'pear', 'orange']
dinner = copy.deepcopy(fruit)
fruit[2] = 'mango'
print('fruit: {}, dinner: {}'.format(fruit, dinner))

# simple class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Logan", 30)
p1.myfunc()