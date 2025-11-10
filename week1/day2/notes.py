# new_list = ['apple', 'banana', 'cherry',[1, 2, 3]]
# print(new_list[3])
# print(new_list[3][0]) 

# grid = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]
# print(grid[0][0])

# my_hobbies = ["Eat", "Sleep", "Code"]
# my_hobbies[0] #Eat
# my_hobbies[1] = "Meditate" #Change "Sleep" to "Meditate"
# my_hobbies.append("Baseball")
# my_hobbies.remove("Meditate")

# my_hobbies = ["Food", "Code"]
# additional_hobbies = ["Sport", "More code"]
# my_hobbies + additional_hobbies 
# ["Food", "Code", "Sport", "More code"]

# list1 = [5, 10, 15, 20, 25, 50, 20]
# index_20 = list1.index(20)
# print(index_20)

# tup = (1, 2, 3, 4, 5)
# print(tup)
# a,b,c,d,e = tup
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# a,*b, = tup
# print(b)

# s = set([1,2,2,3,4,4,5])
# print(s) #{1, 2, 3, 4, 5}

#li = [12, 15, 264, 234, 12, 577,109]
# for item in li:
#     if item > 200:
#         print('Big number is',item)
#     else:
#         print('Small number is',item)
# my_sum = 0
# for item in li:
#     my_sum = my_sum + item
#     print('Current sum:',my_sum)

# print('Final sum:',my_sum)   

# i = 0
# while i < 10:
#     print('i is now:',i)
#     i += 1 #i = i + 1
# runs = int(input('How many times do you want to run the loop? '))
# while i < runs:
#     print('i is now:',i)
#     i += 1 #i = i + 1

li = [12, 15, 264, 234, 12, 577,109]

j = 0
while j < len(li):
    print('Current item is:',li[j])
    j  = j + 1 #cntr C to stop infinite loop

password = 'secret'
tries = 0 
max_tries = 4

guess = input('Enter password: ')
while guess != password and tries < max_tries:
    print('Wrong password, try again.')
    tries += 1
    guess = input('Enter password: ')
if guess == password:
    print('Correct password.')
else:
    print('Too many incorrect tries.')        

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

li = [12, 15, 264, 234, 12, 577,109]
for item in li:
    if item > 200:
        break
    print('Current item is:',item)        

list = []
x = 1.5
while x <= 5:
    list.append(x)
    x = x + 0.5
print(list)





