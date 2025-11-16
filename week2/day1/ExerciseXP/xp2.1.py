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
    def __init__(self, lyrics)
        self.lyrics = lyrics

 def sing_ma_a_song(self):
    for line in self.lyrics:
        print(line)



stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

#Output: There’s a lady who’s sureall that glitters is goldand she’s buying a stairway to heaven


    
     