#len('Anna')
# name = 'Anna'
#name.upper()
#print(name.upper())
#sentence = 'I love Python\n'
#print(sentence * 3)
#sentence_js = sentence.replace('Python', 'JavaScript')
#print(sentence_js)
#price = '15$'
#clean_price = price.replace('$', '')
#clean_price = int(clean_price)
#print(clean_price)

#name_upper = name.upper()
#print(name_upper)

#description = "strings are sequence of characters"
#print(description.upper())
#new_description = description.replace('are', 'is')
#print(new_description)
#print(description[:7])

#f_name = 'Harry'
#l_name = 'Potter'
#age = 15
#address = '4 Privet Drive'
#is_wizzard = True

#x = 1
#y = 2
#t = x
#x = y
#y = t


#print(x)
#print(y) 

#user_name = input('Enter your name: ')
#print(user_name)
#user_age = int(input('Enter your age: '))
#print(user_age + 10)
#print(f'{user_name} is {user_age} years old')
#count = 0
#user_name = input('Enter your name: ')
#count += 1
#print(user_name)
#print(count)

#

client_age = int(input('What\'s your age: '))
if client_age < 12:
    print('Sorry, you can\'t see this movie')
if client_age < 7:
    print('We will call your parents')    
elif client_age > 13 and client_age < 16:
    print('You can see this movie with your parents')
elif client_age >= 16:
    print('Enjoy the movie!')
