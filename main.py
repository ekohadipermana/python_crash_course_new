'''
Created by Eko Hadi Permana
This main.py containing all tricks and exercise during the learning
Book: Python Crash Course 2023
Author: Eric Matthes
Publisher: No Starch Press

===========IMPORTANT!!!!!=========
How to use this file:
DO NOT RUN THIS WHOLE FILE AT ONCE! You will get an error!
Just block the lines you want to execute then execute the selection in Python Console
or ALT+SHIFT+E
'''


REMINDER = '''
=====================
YOU DON'T HAVE UNLIMITED TIME FOR EVERYTHING!
THE CLOCK IS TICKING!
=====================
'''

print('Hello World')
message = 'Hello World in a variable' # using variable
print(message)

message = 'This is the new content of variable message'
print(message)

name = 'thOriN oakenshield'
name_1 = name.title()
print(name_1)
print(name.upper())
print(name.lower())

first_name = 'frodo'
last_name = 'baggins'
full_name = f'{first_name} {last_name}'
print(full_name.title())
print(f'Hello, my name is {full_name.title()}')

print('this\tis\tthe\tname\tof\tthe\tFellowships')
print('Frodo Baggins\nSamwise Gamgee\nMeriadock Brandibuck\nPeregrin Took')

name_2 = 'Aragorn '
name_3 = '   Elessar'
print(f'{name_2}{name_3}')

# using rstrip (right strip) or lstrip (left strip)
print(f'{name_2.rstrip()}{name_3.rstrip()}')

# using strip
print(f'{name_2.strip()}{name_3.strip()}')

# removing prefixes
name_4 = 'Mr/Mrs Boromir of Gondor'
print(name_4.removeprefix('Mr/Mrs '))

# removing suffixes
print(name_4.removesuffix(' of Gondor'))

# integer number
print(3 + 7)

num_1 = 15_000
num_2 = 10_000

# addition and subs
print(num_1 + num_2)
print(num_1 - num_2)

# multiplication and div
print(num_1 * num_2)
print(num_2 / num_1)

# exponent
print(2 ** 3)

# the PEMDAS
the_float = 8 / 2
print(type(the_float)) # division always results float

# multiple assignments
x, y, z = 2, 3, 4
a = x + y + z
print(a)

# write constants in capitals
MAX_INPUT = 10_000

fav_num = 99
print(f'This is my favorite number: {fav_num}')

# The List
the_fellowships = ['Frodo', 'Sam', 'Merry', 'Pippin', 'Aragorn', 'Boromir', 'Legolas', 'Gimli', 'Gandalf']
print(len(the_fellowships))
print(the_fellowships)
print(the_fellowships[8].upper())
print(the_fellowships[-2])
print(f'One of the member of the nine fellowships is: {the_fellowships[5]}')
the_fellowships[5] = 'Thorin' # changing the value of position 5 from Boromir to Thorin
print(the_fellowships)

the_fellowships.append('Boromir')  # appending an element to the end of the list
print(the_fellowships)

the_fellowships.insert(0, 'Bilbo')
print(the_fellowships)

print(REMINDER)

print(the_fellowships)
del the_fellowships[5]  # deleting element 5 (aragorn)
print(the_fellowships)

deceased_person = []
deceased_person.append(the_fellowships.pop())  # popping an item (last one)
print(the_fellowships)
print(deceased_person)
deceased_person.append(the_fellowships.pop(0))  # popping an item by its position
print(deceased_person)

deceased_person.remove('Boromir')  # removing item by value
print(deceased_person)

the_complete_fellowships = ['Frodo', 'Sam', 'Merry', 'Pippin', 'Aragorn', 'Boromir', 'Legolas', 'Gimli', 'Gandalf']
the_complete_fellowships.sort()  # sorting the list permanently
print(the_complete_fellowships)

the_complete_fellowships.sort(reverse=True)  # reversed sort
print(the_complete_fellowships)

print(f'This is sorted temporarily: {sorted(the_complete_fellowships)}')
print(f'This is the original: {the_complete_fellowships}')

frodos_friends = ['sam', 'merry', 'pippin', 'gaffer']
frodos_friends.reverse()  # this is just reversing the order of the items, not alphabetically
print(frodos_friends)

print(len(the_complete_fellowships))  # find the length of a list

# Chapter 4 - Working with lists
for fellow in the_complete_fellowships:  # looping through all items in a list
    print(f'This is {fellow.upper()}')
print('That is all')

# Making numerical list page 56
# Started on Sunday, October 1, 2023, 10.42

# using the range() function
for value in range(1, 5):  # range off by one, 5 not included
    print(value)

# using range() to make a list of numbers
_numbers = list(range(1, 6))
print(_numbers)

# making a list of first ten exponents using range()
first_exponents = []
for i in range(1, 11):
    i = i ** 2
    first_exponents.append(i)
print(first_exponents)

# or use this more concise method:
first_exponents = []
for i in range(1, 11):
    first_exponents.append(i ** 2)
print(first_exponents)

# simple statistics with list
list_100 = []
for i in range(1, 101):
    list_100.append(i)
print(list_100)
print(min(list_100))
print(max(list_100))
print(sum(list_100))

# List comprehensions
first_exponents_comp = [i ** 2 for i in range(1, 11)]
print(first_exponents_comp)

# exercise
# counting to 20:
for i in range(1, 21):
    print(i)

# make a list of one million:
million = [i for i in range(1, 1_000_001)]
print(million)

# summing a million"
print(sum(million))

# make a list of odd numbers using the third argument of range
_numbers_0 = [i for i in range(1, 21, 2)]
print(_numbers_0)

# list of multiple of threes from 3 to 30:
threes = [i * 3 for i in range(3, 31)]
print(threes)

# list of the first ten cubes (third power):
cubes = [i ** 3 for i in range(1, 11)]
print(cubes)

# Working with part of a list (page 61):
# slicing a list
players = ['Frodo', 'Sam', 'Merry', 'Pippin', 'Thorin', 'Legolas', 'Gimli', 'Gandalf']
print(players[0:3])  # from 0 to 2 (just like range)
print(players[2:5])

# slicing from the beginning of a list to 3 use [:4]
print(players[:4])

# slicing from some item to the end:
print(players[2:])

# negative number means the last 3 item to the end (imagine the number ruler)
print(players[-3:])

# Looping through a slice (page 62)
players = ['Frodo', 'Sam', 'Merry', 'Pippin', 'Thorin', 'Legolas', 'Gimli', 'Gandalf']
for player in players[1:6]:
    print(player)

# copying a list
player_some = players[:]  #  can be like this too: player_some = players[:]
print(player_some)
players.append('Glorfindel')
player_some.append('Ugluk')
print(f'this is players {players}')
print(f'this is player_some {player_some}')

# Tuples page 65
# tuple is immutable, you can't change the items
the_coordinate = (200, 300, 250, 720, 1280)
for item in the_coordinate:
    print(item)

# insight: can you make a list from slicing a tuple?
# answer is can't because the result will be a tuple
coordinate_list = []
coordinate_list.append(the_coordinate[:4])
print(coordinate_list)

# but this would do using looping:
coordinate_list = []
for i in the_coordinate:
    coordinate_list.append(i)
print(coordinate_list)

#  although you can't change a tuple, you can redefine a tuple
print(f'original tuple: {the_coordinate}')
the_coordinate = (1000, 1000)
print(f'this is the modified tuple {the_coordinate}')

# Chapter 5 IF statements page 71

cars = ['audi', 'BMW', 'tesla', 'toyota']
for car in cars:
    if car.upper() == 'BMW':
        print(car.lower())
    else:
        print(car.title())

#  conditional test using Boolean result True or False
requested_topping = 'ChocolatE'
correct_topping = 'chocolate'
if requested_topping.lower() == correct_topping:
    print('The topping is correct')
else:
    print('the topping is incorrect')

# checking for numerical comparisons:
number_one = 250
correct_number = 999
if number_one != correct_number:
    print('The number is incorrect')
else:
    print('The number is correct')

# other comparison operators are: <, >, <=, >=

# checking multiple condition using "and"
number_two = 60
upper_num = 70
lower_num = 50
if number_two >= 50 and lower_num <= upper_num:
    print('the number is within the range')
else:
    print('the number is out of range')

# checking multiple condition using "or"
level_checking = 4
if level_checking == 1 or level_checking == 4:
    print('The level is correct')
else:
    print('the level is incorrect')

#  checking whether a value is in a list using "in" or "not in"
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print('in the requested toppings')
else:
    print('not in requested toppings')

# deeper with if-elif-else statements
the_number = 40
if the_number == 10:
    print('the number is 10')
elif the_number == 20:
    print('the number is 20')
elif the_number == 30:
    print('the number is 30')
else:
    print('the number is neither 10, 20, or 30')

'''Exercise:
1. alien colors: : Imagine an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the alien’s color is green. If it is, print
a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that
fails. (The version that fails will have no output.)
 '''
alien_color = 'blue'
if alien_color == 'green':
    print('You got 5 points')
elif alien_color == 'red':
    print('You got 10 points')
elif alien_color == 'blue':
    print('You got 15 points')

#  stages of life:
the_age = 44
if the_age < 2:
    print('It is a baby')
elif the_age >= 2 and the_age < 4:
    print('It is a toddler')
elif the_age >= 4 and the_age < 13:
    print('It is a kid')
elif the_age >= 13 and the_age < 20:
    print('It is a teenager')
elif the_age >= 20 and the_age < 65:
    print('It is an adult')
elif the_age > 65:
    print('It is an elder')

#  check if the list empty or not:
topping_list = []
if topping_list:
    for topping in topping_list:
        print(topping)
else:
    print('the list is empty')

# using multiple lists
coffee_list = ['cappuccino', 'espresso', 'black', 'latte']
requested_coffee = ['cappuccino']
if requested_coffee in coffee_list:
    print('Coffee will be served')
else:
    print('Sorry, the requested coffee is unavailable')

# DICTIONARIES CHAPTER 6, page 91
# a simple dictionary:
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# adding a key-value to a dictionary
# simply add key-value
alien_0['level'] = 'advanced'
print(alien_0)

# you can start with an empty dict just like a list
alien_1 = {}
print(alien_1)
alien_1['rating'] = 'good'
alien_1['level'] = 10
print(alien_1)
# modify the value by directly change it
alien_1['level'] = 7
print(alien_1)

# removing a key-value:
del alien_1['level']
print(alien_1)

# multiple key-values:
the_fellowships_dict = {
    'Frodo': 'Hobbit',
    'Sam': 'Hobbit',
    'Gimli': 'Dwarf',
    'Gandalf': 'Wizard'
}
print(f'The race of Gandalf is {the_fellowships_dict["Gandalf"]}')

#  using get() to access values, page 97
# get(), first arg: the key, 2nd arg: what to do if it does not exist
member_name = the_fellowships_dict.get('Gimli', 'Member name does not exist')
print(member_name)

# looping through all key-value pairs
for name, race in the_fellowships_dict.items():
    print(f'name: {name}, race: {race}')

# looping through all the keys in a dictionary, page 101
for name in the_fellowships_dict.keys():
    print(name)

# looping through the keys with a particular order
for name in sorted(the_fellowships_dict.keys()):
    print(name)
print(the_fellowships_dict)

# looping through all values in a dictionary
for race in the_fellowships_dict.values():
    print(race)

# Nesting a dictionary
# A list of dictionaries
hobbits = {
    'frodo': 'baggins',
    'sam': 'gamgee',
    'meriadoc': 'brandybuck',
    'peregrin': 'took'
}
wizards = {
    'gandalf': 'unknown',
    'saruman': 'isengard'
}
characters_0 = [hobbits, wizards]
for character in characters_0:
    print(character)

# a list in a dictionary
the_consuls = {
    'hobbits': ['frodo', 'sam', 'pippin', 'merry'],
    'elves': ['elrond', 'legolas', 'galadriel'],
    'men': ['aragorn', 'boromir', 'faramir']
}
print(the_consuls)
for race, names in the_consuls.items():
    print(race)
    for name in names:
        print(f'\t{name}')

# a dictionary in a dictionary
users = {
    'men': {
        'first': 'aragorn',
        'last': 'elessar',
        'origin': 'numenor'
    },
    'hobbit': {
        'first': 'frodo',
        'last': 'baggins',
        'origin': 'shire'
    }
}
print(users['men']['first'])

# CHAPTER 7, USER INPUT AND WHILE LOOPS, page 113

message = input('Tell me something and i will repeat it:')
print(message)

name = input('please enter your name:\n')
print(f'Hello, {name.title()}')

# using int() to accepts numerical input
number = int(input('Enter a number from 1 to 100:\n'))
print(number)
print(type(number))

# modulo operator
if number % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')

# introducing while loops, page 117
current_num = 1
while current_num < 20:
    print(current_num)
    current_num += 1
print('Done')

# let the user control the loop
# this version is too complicated for me!
the_prompt = input("Type something and I will repeat it back:\n")
the_prompt += '\nEnter quit to exit'.lower()
message = ''
while message != 'quit':
    message = input(the_prompt)
    print(message)
print('Thank You')

# here's my own way:
is_on = True  # this is what you call a flag
while is_on:
    the_question = input("Type something and I will repeat it back or type quit to end:\n")
    if the_question == 'quit':
        is_on = False
    else:
        print(the_question)

# using break to exit a loop (no need a flag)
while True:  # just use this while true for a loop
    the_question = input("Type something and I will repeat it back or type quit to end:\n")
    if the_question == 'quit':
        print('The program will quit. Thank You')
        break
    else:
        print(the_question)

# using continue in a loop
current_num = 0
while current_num <= 10:
    current_num += 1
    if current_num % 2 == 0:  # if the current_num is even,
        continue              # it loop back to the beginning of 'while' using 'continue'

    print(current_num)  # if the current_num is odd, it will be printed

''' Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping, print 
a message saying you’ll add that topping to their pizza.'''
topping_list = []
while True:
    theTopping = input('Please enter a topping or type "x" when you finish:\n')
    if theTopping == 'x':
        print('The topping for your pizza would be:\n')
        for topping in topping_list:
            print(topping)
        break
    else:
        topping_list.append(theTopping)

'''Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
'''
# This code produced an error
while True:
    age = int(input('What is your age:\n'))
    if age < 3:
        print('Free ticket')
    elif age >= 3 and age <= 12:
        print('$10 ticket')
    elif age > 12:
        print('$15 ticket')
    elif age == 'quit':  # this line: the conversion of str to int caused error
        break

# This is the revision, error free
while True:
    age = input('What is your age:\n')  # not converted to int in the beginning
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print('Free ticket')
    elif age >= 3 and age <= 12:
        print('$10 ticket')
    elif age > 12:
        print('$15 ticket')

# Using a while loop with Lists and Dictionaries, page 124
# moving items from one list to another
# this is my code:
unverified_users = []
verified_users = []
while True:
    users = input('Enter a user name (quit to finish):\n')
    if users == 'quit':
        break
    else:
        unverified_users.append(users)
for user in unverified_users:
    confirmed = input(f'Is this name: {user} verified?')
    if confirmed == 'y':
        verified_users.append(user)
print('The list of verified users:\n')
for user in verified_users:
    print(f'\t{user}')

# this is the code from the book:
# Start with users that need to be verified,
#  and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
#  Move each verified user into the list of confirmed users.
while unconfirmed_users:  # this "while" keeps running until it's empty
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Removing all instances of specific values from a list, page 125
# this code removes all the word "cat" from the list:
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while 'cat' in pets:  # while cat still in pets
    pets.remove('cat')  # remove it
print(pets)

# filling a dictionary with user input, page 125 (finish 13.01, 1 hour 45 min)
responses = {}
while True:
    name = input('Enter your name:\n')
    if name == 'quit':
        break
    _class = input('Enter your level:\n')
    responses[name] = _class
    print('Recorded successfully.')

print('Responders:\n')
for name, level in responses.items():
    print(f'Name: {name.title()}')
    print(f'\tLevel: {level.title()}')

''' --------- EXERCISES ----------
Deli: Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop through
the list of sandwich orders and print a message for each order, such as I made
your tuna sandwich. As each sandwich is made, move it to the list of finished
sandwiches. After all the sandwiches have been made, print a message listing
each sandwich that was made.'''
sandwich_orders = ['tuna sandwich', 'cheese sandwich', 'beef sandwich',
                   'chocolate sandwich', 'peanut sandwich']
finished_sandwiches = []
while sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    print(f'I made your {made_sandwich} order')
    finished_sandwiches.append(made_sandwich)
print('Made sandwiches list:')
for sandwich in finished_sandwiches:
    print(f'\t{sandwich}')

''' --------- EXERCISES ----------
No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.'''
sandwich_orders = ['tuna sandwich', 'cheese sandwich', 'beef sandwich',
                   'chocolate sandwich', 'peanut sandwich', 'pastrami',
                   'pastrami', 'pastrami']
finished_sandwiches = []
print('Pastrami is unavailable')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    print(f'I made your {made_sandwich} order')
    finished_sandwiches.append(made_sandwich)
print('Made sandwiches list:')
for sandwich in finished_sandwiches:
    print(f'\t{sandwich}')

# CHAPTER 8 FUNCTIONS, page 129

# a simple function:
def greet_user():  # This is the function
    '''Display a simple greeting'''
    name = input('Enter your name:\n')
    print('========================')
    print(f'Hello, {name.title()}!')
    print('========================')
greet_user()

# passing information to a function
def greet_user_0(name):  # 'name' is a parameter
    '''Display a simple greeting with a parameter and argument'''
    print('========================')
    print(f'Hello, {name.title()}!')
    print('========================')

greet_user_0('gandalf')  # 'gandalf' is an argument
names = ['eko', 'hadi', 'permana', 'anu', 'kasep', 'tea']
for name in names:
    greet_user_0(name)

# Passing arguments, page 131
# Positional arguments
def describe_fellow(name, race):
    """Display information about the fellowship member"""
    print(f'{name.title()} is a/an {race.title()}.')

describe_fellow('gandalf', 'wizard')  # you have to give the correct position for every argument

# keyword arguments
# you don't have to correctly order the argument
describe_fellow(race='hobbit', name='samwise')  # just type the parameter "name="

# default values, page 134
def describe_origin(name, place='middle earth'):
    """Describe origin with a defaut place value"""
    print(f'{name.title()} is from {place.title()}')

describe_origin('Aragorn', "gondor")

# exercises page 136
# add a comment to tes

# start learning 20231108, wed, 11.35

# page 137, Return Values

def get_formatted_name(first_name, last_name):
    """Return a full name neatly formatted"""
    full_name = f'{first_name} {last_name}'
    return full_name.title()

musician = get_formatted_name('jimi', 'hEndriX')
print(musician)

# Returning a Dictionary, p 139

def build_person(first_name, last_name):
    """Return a dictionary of information about a person"""
    person = {'first': first_name.title(), 'last': last_name.title()}
    return person

musician = build_person('jImI', 'hendRix')
print(musician)
