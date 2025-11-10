#1
multiples = []

number = int(input('Enter a random number:'))
length = int(input('Enter a length:'))

for x in range(1, length + 1):
        multiples.append(int(number) * x)
        
print(multiples)

#2
user_string = input('Enter a word: ')
result_string =  user_string[0]

for char in user_string[1:]:
    if char != result_string[-1]:
        result_string += char
print(result_string)