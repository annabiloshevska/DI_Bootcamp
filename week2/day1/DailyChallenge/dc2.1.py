#Daily challenge: Old MacDonald’s Farm
# Create a class called Farm.
# This class will represent a farm and its animals.

# The Farm class should have an __init__ method.
# It should take one parameter: farm_name.
# Inside __init__, create two attributes: name to store the farm’s name and 
# animals to store the animals (initialize as an empty dictionary).
class Farm:
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animals = {}

#Create a method called add_animal.
# It should take two parameters: animal_type and count (with a default value of 1). 
# Count is the quantity of the animal that will be added to the animal dictionary.
# The dictionary will look like this:
# {'cow': 1, 'pig':3, 'horse': 2}
# If the animal_type already exists in the animals dictionary, increment its count by count.
# If it doesn’t exist, add it to the dictionary as the key and with the given count as value.
    
    def add_animal(self, animal_type, count = 1):
       
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count   

# Create a method called get_info.
# It should return a string that displays the farm’s name, 
# the animals and their counts, and the “E-I-E-I-0!” phrase.
# Format the output to match the provided example.
# Use string formatting to align the animal names and counts into columns.
    def get_info(self):
        info = f'{self.farm_name} Farm\n'
        for animal, count in self.animals.items():
            info += f'{animal}:{count}\n'
        info += 'E-I-E-I-0!'
        return info    


# Create a Farm object and call the add_animal and get_info methods.
# Verify that the output matches the provided example.
# Test the code 
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

