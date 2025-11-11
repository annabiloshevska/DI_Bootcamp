#Exercise 1: Converting Lists into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
sample_dict = dict(zip(keys, values))
print(sample_dict)

#Exercise 2: Cinemax #2
total_price = 0
family = {'rick': 43, 'beth': 13, 'morty': 5, 'summer': 8}
for key, value in family.items():
    if 1 <= value <= 3:
        total_price += 0
        print(f'The ticket for {key} is free.')
    elif 3 <= value <= 12:
        total_price += 10
        print(f'The ticket price for {key} is $10.')
    elif value >= 12:
        total_price += 15
        print(f'The ticket price for {key} is $15.')
print(f'Total ticket price for the family is: $ {total_price}')

#Exercise 3: Zara

brand = {'name': 'Zara',
         'creation_date': 1975,
         'creator_name': 'Amancio Ortega Gaona',
         'type_of_clothes': ['men', 'women', 'children', 'home'],
         'international_competitors': ['Gap', 'H&M', 'Benetton'],
         'number_stores': 7000,
         'major_color':{'France': 'blue','Spain':'red','US': ['pink', 'green']}}

brand['number_stores'] = 2
print(f'Number of stores: {brand["number_stores"]}')
print(f'Zara\'s clients are: {brand["type_of_clothes"][0:3]}')
brand['country_creation'] = 'Spain'
if brand.get('international_competitors'):
    brand['international_competitors'].append('Desigual')
del brand['creation_date']
print(brand['international_competitors'][-1])
print(brand['major_color']['US'])    
num_keys = len(brand)
print(f'Number of keys in the brand dictionary: {num_keys}')
for key in brand.keys():
    print(key)

# Exercise 4: Disney Characters    
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
disney_characters_1 = {}

for index_value, char_key in enumerate(users):
    disney_characters_1[char_key] = index_value
print(disney_characters_1)

disney_characters_2 = {}
for index_key, char_value in enumerate(users):
    disney_characters_2[index_key] = char_value
print(disney_characters_2)

sorted_keys = sorted(users)
print(sorted_keys)
disney_characters_sorted = {}
for index_value, key in enumerate(sorted_keys):
    disney_characters_sorted[key] = index_value
print(disney_characters_sorted)  

 



       