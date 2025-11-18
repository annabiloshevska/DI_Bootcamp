#Exercise 1: Currencies
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f'{self.amount} {self.currency}s'

    def __repr__(self):
        return str(self)

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        elif isinstance(other, int):
            return self.amount + other
        else:
            raise TypeError("Unsupported type for addition")

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        elif isinstance(other, int):
            self.amount += other
        else:
            raise TypeError("Unsupported type for in-place addition")
        return self
# Using the code above, implement the relevant methods and dunder methods which will 
# output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)
print(c1)
# '5 dollars'
print(int(c1))
# 5
print(repr(c1))
# '5 dollars'
print(c1 + 5)
# 10
print(c1 + c2)
# 15
print(c1) 
# 5 dollars
c1 += 5
print(c1)
# 10 dollars
c1 += c2
print(c1)
# 20 dollars
#print(c1 + c3)
# TypeError: Cannot add between Currency type <dollar> and <shekel>

#Exercise 2: Import a Function from Another File
from func import add_numbers

print(add_numbers(3, 4))

# Exercise 3: Random String of 5 Letter
import string
import random

letters = string.ascii_letters
#print(letters)  
random_string = ''.join(random.choice(letters) for char in range(5))
print(random_string)

# Exercise 4: Current Date
import datetime

today = datetime.date.today()
print(f'Today\'s date: {today}')

#Exercise 5: Amount of time left until January 1st

#today = datetime.date.today()
#print(f'Today\'s date: {today}')

specific_date = datetime.date(2026, 1, 1)

time_difference = (specific_date - today).days
print(f'Day\'s till January 1st:{time_difference}')

#Exercise 6: Birthday and minutes
# Create a function that accepts a birthdate as an argument (in the format of your choice),
# then displays a message stating how many minutes the user lived in his life.

def birthday():
    user_birthday = input('Enter your birthday(YYYY-MM-DD):')
    birth_date = datetime.datetime.strptime(user_birthday, '%Y-%m-%d').date()
    print(birth_date)

    today = datetime.date.today()
    days_lived = (today - birth_date).days
    minutes_lived = days_lived * 24 * 60
    print(f'You have lived {minutes_lived} minutes in your life.')

#birthday()
# Exercise 7: Faker Module

#Step 1: Install the faker module
#Step 2: Import the faker module
from faker import Faker
fake = Faker()
print(fake.name())
print(fake.address())
print(fake.email())

#Step 3: Create an empty list of users
user_list = []
#Step 4: Create a function to add users

# Create a function that takes the number of users to generate as an argument.
# Inside the function, use a loop to generate the specified number of users.
# For each user, create a dictionary with the keys name, address, and language_code.
# Use the faker instance to generate fake data for each key:
# name: faker.name()
# address: faker.address()
# language_code: faker.language_code()
# Append the user dictionary to the users list.
# Step 5: Call the function and print the users list

def adding_users(num_of_users):
    for item in range(num_of_users):
        user = dict()
        user['name'] = fake.name()
        user['address'] = fake.address()
        user['language_code'] = fake.language_code()
        user_list.append(user)

adding_users(3)
print(user_list)


