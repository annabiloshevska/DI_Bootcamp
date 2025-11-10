#1
my_fav_numbers = {1,3,5}
my_fav_numbers.add(7)
my_fav_numbers.add(10)
my_fav_numbers.remove(10)
print(my_fav_numbers)

friend_fav_numbers = {2,4,6}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)
#2
my_tuple = (1, 2, 3)
my_tuple = my_tuple + (4, 5)
print(my_tuple)
#3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
basket.count("Apples")
basket.clear()
print(basket)
#4
list = []
x = 1.5
while x <= 5:
    list.append(x)
    x = x + 0.5
print(list)
#5
nums_list = []
for i in range(1, 21):
    nums_list.append(i)
print(nums_list)

nums_list2 = []
for i in range(1, 21):
    if i % 2 == 0:
        nums_list2.append(i)
print(nums_list2)
#6
while True:
    user_name = input('Enter your name: ')
    if not user_name.isdigit() and len(user_name) >= 3:
        print('Thank you:', user_name)
        break
    else:
        print('Invalid name, please try again.')

#7
toppings = []

while True:
    user_topping = input('Enter pizza toppings one by one (type "quit" to finish): ') 
    if user_topping == 'quit':
        break
    print(f'Adding {user_topping}, to your pizza')
    toppings.append(user_topping)

 
print('Your pizza will contain these toppings:')
for topping in toppings:
        print(f'- {topping}')

base_price = 10
topping_price = 2.5
amount_of_toppings = len(toppings)
total_price = (base_price + topping_price * amount_of_toppings)


print(f'Total price is: $ {total_price}')

#9
total_price = 0
while True:
    client_age = int(input('Enter the age of each person in a family who wants to buy a movie ticket(type "0" to finish): '))
    if client_age == 0:
        break
    if 1 <= client_age <= 3:
        print('The ticket is free.')
        total_price += 0
    elif 3 <= client_age <= 12:
        print('The ticket price is $10.')
        total_price += 10
    else:
        print('The ticket price is $15.')
        total_price += 15


print(f'Total ticket price for the family is: $ {total_price}')        