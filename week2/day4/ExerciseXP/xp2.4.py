#Exercise 1: Random Sentence Generator
import os
import random

dir_path = os.path.dirname(os.path.realpath(__file__))

# Create a function named get_words_from_file that takes the file path as an argument.
# Open the file in read mode ("r").
# Read the file content.
# Split the content into a list of words.
# Return the list of words.

def get_words_from_file():

    with open(os.path.join(dir_path, 'words.txt'), 'r') as f:
        words = f.read().split()
        return words
# Create a function named get_random_sentence that takes the sentence length as an argument.
# Call get_words_from_file to get the list of words.
# Select a random word from the list length times.
# Create a sentence with the selected words.
# Convert the sentence to lowercase.
# Return the sentence.
def get_random_sentence(sent_length):
    words = get_words_from_file()
    selected_words = []
    for word in range(sent_length):
        selected_words.append(random.choice(words))
    rand_sentence = (' '.join(selected_words).lower())
    return rand_sentence

# Create a function named main.
# Print a message explaining the program’s purpose.
# Ask the user for the desired sentence length.
# Validate the user input:
# Check if it is an integer.
# Check if it is between 2 and 20 (inclusive).
# If the input is invalid, print an error message and exit.
# If the input is valid, call get_random_sentence with the length and print the generated sentence.
def main():
    print('This program will generate a random sentence.')
    while True:
        sent_length = int(input('Enter the desired sentence length(from 2 to 20):'))
        if sent_length not in range(2, 21):
            print('Invalid input')
            break
        else:
            result = get_random_sentence(sent_length)
            print(result)
        
main()
#Exercise 2: Working with JSON

import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


# Import the json module.
# Use json.loads() to parse the JSON string into a Python dictionary.
data = json.loads(sampleJson)

# Access the “salary” key using nested dictionary access (e.g., data["company"]["employee"]["payable"]["salary"]).
# Print the value of the “salary” key.
salary1 = data["company"]["employee"]["payable"]["salary"]
print(salary1)
# Add a new key-value pair to the “employee” dictionary: "birth_date": "YYYY-MM-DD".
# Replace "YYYY-MM-DD" with an actual date.

data["company"]["employee"]['birth_date'] = '2000-01-15'
# Open a file in write mode ("w").
# Use json.dump() to write the modified dictionary to the file in JSON format.
# Use the indent parameter to make the JSON file more readable.
with open(dir_path + '\data.json', 'w') as f:
    json.dump(data, f, indent = 4)
    print('file was created')

        


