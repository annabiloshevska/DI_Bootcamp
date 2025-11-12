# Exercise 1: What are you learning?
def display_message():
    print('I am learning about functions in Python.')
display_message()    

#Exercise 2: What’s Your Favorite Book?
def favoirite_book(title):
   print(f'One of my favorite books is {title}')
favoirite_book('Harry Potter') 

#Exercise 3: Some Geography
def describe_city(city, country='Unknown'):
  return

describe_city('Reykjavik', 'Iceland')
describe_city('Paris')

#Exercise 4: Random
import random

def random_num_game():
    user_num = (input('Your number:'))

    rand_num = random.randint(1,100)
    if user_num == rand_num:
       print('Success!')
    else:
       print(f'Fail. Your number:{user_num}, Random number:{rand_num}')

random_num_game()
   
#Exercise 5: Let’s Create Some Personalized Shirts!

def make_shirt(size = 'large', text = 'I love Python'):
   print(f'Your shirt\'s size is {size}.{text}')
#calling the function
make_shirt('M', 'Cute!')
#calling with large shirt and default mmessage
make_shirt()
#calling with medium and and default mmessage
make_shirt('medium')
#calling with default and custom message
make_shirt(text = 'Cute!')

#Exercise 6: Magicians

# Create a list called magician_names with the given names:
# Create a function called show_magicians() that takes the magician_names list as a parameter.
# Inside the function, iterate through the list and print each magician’s name.
# Create a function called make_great() that takes the magician_names list as a parameter.

# Inside the function, use a for loop to iterate through the list and add “the Great” before each magician’s name.
# Call make_great() to modify the list.
# Call show_magicians() to display the modified list.
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
print(magician_names)

def show_magicians(magician_names):
    for mag in magician_names:
       print(mag)

def make_great(magician_names):
   for i, mag in enumerate(magician_names):
      magician_names[i] = 'the Great ' + mag

show_magicians(magician_names)
make_great(magician_names)
show_magicians(magician_names)


# Exercise 7: Temperature Advice

#Create a function called get_random_temp() that returns a random integer between -10 and 40 degrees Celsius.
# Create a function called main(). Inside this function:
# Call get_random_temp() to get a random temperature.
# Store the temperature in a variable and print a friendly message
# # Inside main(), provide advice based on the temperature
def get_random_temp():
    temp = random.randint(-10, 40)
    return temp

def main():
    temp = get_random_temp()
    print(f'“The temperature right now is {temp} degrees Celsius.”')
    if temp < 0:
        print('Brrr, that\'s freezing! Wear some extra layers today.')
    elif 0 <= temp <= 16:
        print('Quite chilly! Don’t forget your coat.')   
    elif 17 <= temp <= 23:
        print('Nice weather')
    elif 24 <= temp <= 32:
        print('A bit warm, stay hydrated.')   
    elif 33 <= temp <= 40:
        print('It’s really hot! Stay cool.')        

main()
