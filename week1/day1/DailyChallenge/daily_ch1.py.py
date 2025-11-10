
sentence = input('Enter a sentence(it must be 10 characters long)')

if len(sentence) < 10:
    print('String  is not long enough.')
elif len(sentence) > 10:
    print('String is too long.')
elif len(sentence) == 10:
    print('Perfect string.')

print('The first character is:', sentence[0])
print('The last character is:', sentence[-1])

for char in range(len(sentence) + 1):
    print(sentence[:char])

import random
list_sentence = list(sentence)

random.shuffle(list_sentence) 
jumbled = "".join(list_sentence)  
print("Jumbled string:", jumbled)

