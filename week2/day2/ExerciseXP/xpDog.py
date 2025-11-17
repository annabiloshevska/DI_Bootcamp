#Exercise 1: Pets
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)
    def sing(self, name, sounds):
        
        return f'{sounds}'

class Chartreux(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)    
    def sing(self, sounds):
        return f'{sounds}'    
# Create a class called Siamese that inherits from the Cat class.
# You can add any specific attributes or methods for the Siamese breed, 
# or leave it as is if there are no unique behaviors.    
class Siamese(Cat):
    def __init__(self, name, age):
        super().__init__(name, age)
    def jump(self):
        print(f'{self.name} jumped')
# Create a list called all_cats that contains instances of Bengal, Chartreux, and Siamese cats.
# Example: all_cats = [bengal_obj, chartreux_obj, siamese_obj]
# Give each cat a name and age.        

bengal1 = Bengal('Simba',3)
chartreux1 = Chartreux('Clementine',2)
siamese1 = Siamese('Noodle',1)
all_cats = [bengal1, chartreux1, siamese1]
# Create an instance of the Pets class called sara_pets, 
# passing the all_cats list as an argument.
sara_pets = Pets(all_cats)
# Call the walk() method on the sara_pets instance.
# This should print the result of calling the walk() method on each cat in the list.
sara_pets.walk()
#_________________________________________________________________________________________
#Exercise 2: Dogs
#Create a class called Dog with name, age, and weight attributes.
#Implement a bark() method that returns “<dog_name> is barking”.
#Implement a run_speed() method that returns weight / age * 10.
#Implement a fight(other_dog) method that returns a string indicating which dog won the fight, based on run_speed * weight.
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'
    
    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f'{self.name} has won the fight against {other_dog.name}'
        else:
            return f'{self.name} has lost the fight. {other_dog.name} wins'

#Create three instances of the Dog class with different names, ages, and weights.
dog1 = Dog('Rex', 5, 15)
dog2 = Dog('Fluff', 6, 8)
dog3 = Dog('Sausage', 3, 7)

#Call the bark(), run_speed(), and fight() methods on the dog instances to test their functionality.
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))
#_________________________________________________________________________________________
# Exercise 4: Family and Person Classes

# Define a Person class with the following attributes:
# first_name
# age
# last_name (string, should be initialized as an empty string)
# Add a method called is_18():
# It should return True if the person is 18 or older, otherwise False.
class Person:
    def __init__(self, first_name, age, last_name):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name
        last_name =  ('')

    def is_18(self):
        if self.age >= 18:
            return True
        else:
            return False
# Define a Family class with:
# A last_name attribute
# A members list that will store Person objects (should be initialized as an empty list)
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []
# Add a method called born(first_name, age):
# It should create a new Person object with the given first name and age.
# It should assign the family’s last name to the person.
# It should add this new person to the members list.        
    def born(self,first_name, age):
        newborn = Person(first_name, age, self.last_name)
        self.members.append(newborn)
# Add a method called check_majority(fi rst_name):
# It should search the members list for a person with that first_name.
# If the person exists, call their is_18() method.
# If the person is over 18, print:
# "You are over 18, your parents Jane and John accept that you will go out with your friends"
# Otherwise, print:
# "Sorry, you are not allowed to go out with your friends."
    def check_majority(self, first_name):
        for person in self.members:    
            if person.first_name == first_name:
                if person.is_18():
                    print('You are over 18, your parents Jane and John accept that you will go out with your friends"')
                else:
                    print('Sorry, you are not allowed to go out with your friends.')
# Add a method called family_presentation():
# It should print the family’s last name.
# Then, it should print each family member’s first name and age.
    def family_presentation(self):
        print(f'Family: {self.last_name}')
        for member in self.members:
            print(f'{member.first_name}, {member.age}') 
# Create a family with a last name.
family1 = Family('Potter')
# Add members to the family using the born() method.
family1.born('John', 36)
family1.born('Jane', 33)
family1.born('Emily', 1)
# Display family information with family_presentation().
family1.family_presentation()
# Use check_majority() to see if someone is allowed to go out.
family1.check_majority('Emily')
# Don’t forget to test your classes by creating an instance of Family, adding members, and calling each method to see the expected output.






