print('Hello world\n' *4)
result = (99^3)*8
print(result)

5 < 3 #False
3 == 3 #True
3 == "3" #False
#"3" > 3 #Error
"Hello" == "hello" #False

computer_brand = "Lenovo"
print(f'I have a {computer_brand} computer')

name = 'Anna'
age = 29
shoe_size = 38
info = f'My name is {name}, I am {age} years old and my shoe size is {shoe_size}'
print(info)

a = 2
b = 1
if a > b:
    print('Hello World')

number = int(input('Please, enter a number:'))
if number % 2 == 0:
    print('This is an even number')
else: 
    print('This is an odd number')

user_name = input('Enter your name: ')
if user_name == 'Anna':
    print('Hello, Anna! My name is also Anna!')
else:
    print(f'Hello, {user_name}!')

rider_height = int(input('Enter your height in cm: '))
if rider_height >= 145:
    print('You are tall enough to ride the rollercoaster!')   
else:
    print('Sorry, you need to grow some more to ride the rollercoaster.')       