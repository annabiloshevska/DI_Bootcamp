#Exercise 1 Cats
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


# Step 1: Create cat objects
cat1 = Cat('Wiskers', 3)
cat2 = Cat('Meow',5)
cat3 = Cat('Boss',6)

# Step 2: Create a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    # ... code to find and return the oldest cat ...
    oldest_cat = cat1
    if cat2.age > oldest_cat.age:
        oldest_cat = cat2
    if cat3.age > oldest_cat.age:
        oldest_cat = cat3
    return oldest_cat

oldest_cat = find_oldest_cat(cat1, cat2, cat3)
# Step 3: Print the oldest cat's details       
print(f'The oldest cat is {oldest_cat.name}, he\'s {oldest_cat.age} years old.')

#Exercise 2 : Dogs

#Create a class called Dog.
# In the __init__ method, take name and height as parameters and create corresponding attributes.
# Create a bark() method that prints “<dog_name> goes woof!”.
# Create a jump() method that prints “<dog_name> jumps <x> cm high!”, where x is height * 2.
class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height
    
    def bark(self):
        print(f'{self.name} goes woof!')
    def jump(self):
        x = self.height * 2
        print(f'{self.name} jumps {x} cm high!')        

#Create davids_dog and sarahs_dog objects with their respective names and heights.
davids_dog = Dog('Lightning', 60)
sarahs_dog = Dog('Sausage', 23)

#Print the name and height of each dog.
#Call the bark() and jump() methods for each dog.
print(f'{davids_dog.name} is {davids_dog.height} cm tall')
print(f'{sarahs_dog.name} is {sarahs_dog.height} cm tall')
davids_dog.bark()
sarahs_dog.bark()
davids_dog.jump()
sarahs_dog.jump()

#Step 4: Compare Dog Sizes

if davids_dog.height > sarahs_dog.height:
    print(f'{davids_dog.name} is bigger that {sarahs_dog.name}')
else:
    print(f'{sarahs_dog.name} is bigger that {davids_dog.name}')

#Exercise 3 : Who’s the song producer?

# Create a class called Song.
# In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
# Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()
#Output: There’s a lady who’s sureall that glitters is goldand she’s buying a stairway to heaven

#Exercise 4 : Afternoon at the Zoo
# 1. Create a class called Zoo.
# 2. Implement the __init__() method:

# It takes a string parameter zoo_name, representing the name of the zoo.
# Initialize an empty list called animals to keep track of animal names.

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animal_names = []
# 3. Add a method add_animal(new_animal):
# This method adds a new animal to the animals list.
# Do not add the animal if it is already in the list.    
    def add_animal(self, new_animal):
        if new_animal in self.animal_names:
            print('This animal is already in the zoo.')
        else:
            self.animal_names.append(new_animal)
            print(f'New animal {new_animal} was added.') 
# 4. Add a method get_animals():
# This method prints all animals currently in the zoo.
    def get_animals(self):
        print(f'Animals currently in the zoo: {self.animal_names}')
# 5. Add a method sell_animal(animal_sold):
# This method checks if a specified animal exists on the animals list and if so, remove from it.
    def sell_animal(self, animal_sold):
        if animal_sold not in self.animal_names:
            print('This animal is not in the zoo.')
        else:
            self.animal_names.remove(animal_sold)
            print(f'{animal_sold} have been sold')    
# 6. Add a method sort_animals():
# This method sorts the animals alphabetically.
# It also groups them by the first letter of their name.
# The result should be a dictionary where:
# Each key is a letter.
# Each value is a list of animals that start with that letter.    

    def sort_animals(self):
        sorted_animals = sorted(self.animal_names)
        grouped_animals = {}
        for animal in sorted_animals:
            first_letter = animal[0]
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = []
            grouped_animals[first_letter].append(animal)
        self.grouped_animals = grouped_animals    
        return grouped_animals    
         
# 7. Add a method get_groups():
# This method prints the grouped animals as created by sort_animals().
    def get_groups(self):
        if not self.grouped_animals:
            self.sort_animals()
        print(f'Grouped animals: {self.grouped_animals}')
        for letter,animals in self.grouped_animals.items():
            print(f'{letter}:{animals}')

# Step 3: Call the Zoo Methods
#Use the methods of your Zoo object to test adding, selling, displaying, sorting, and grouping animals.
# Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups() 