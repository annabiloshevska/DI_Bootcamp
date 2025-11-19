# Daily challenge : Text Analysis

# Create a class called Text.
# The __init__ method should take a string as an argument and store it in an attribute (e.g: self.text).
import os
import string
import re

dir_path = os.path.dirname(os.path.realpath(__file__))

class Text:
    def __init__(self,text):
        self.text = text
# Create a method called word_frequency(word).
# Split the text attribute into a list of words.
# Count the occurrences of the given word in the list.
# Return the count.
# If the word is not found, return None or a meaningful message.
    def word_frequency(self, word):
        list_words = self.text.split()
        if word in list_words:
            return list_words.count(word)
        else:
            return None
# Create a method called most_common_word().
# Split the text into a list of words.
# Use a dictionary to store word frequencies.
# Find the word with the highest frequency.
# Return the most common word.
    def most_common_word(self):
        list_words = self.text.split()
        counts_dict = {}
        most_common = []
        for word in list_words:
            counts_dict[word] = counts_dict.get(word, 0) + 1
        most_common = max(counts_dict, key= counts_dict.get)
        return most_common    
# Create a method called unique_words().
# Split the text into a list of words.
# Use a set to store unique words.
# Return the unique words as a list.
    def unique_words(self):
       list_words = self.text.split()
       unique = set(list_words)
       return list(unique) 
# Create a class method called from_file(file_path).
# Open the file at file_path in read mode.
# Read the file content.
# Create and return a Text instance with the file content as the text.
    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return cls(content)
# Create a method called remove_punctuation().
# Use the string module to get a string of punctuation characters.
# Use a string method or regular expressions to remove punctuation from the text attribute.
# Return the modified text.
class TextModification(Text):
    def remove_punctuation(self):
        modified_text = str.maketrans('', '', string.punctuation)
        return self.text.translate(modified_text)
# Create a method called remove_stop_words().
# Search online for a list of English stop words (common words like “a”, “the”, “is”).
# Split the text into a list of words.
# Filter out stop words from the list.
# Join the remaining words back into a string.
# Return the modified text.
    def remove_stop_words(self):
        stop_words = ['am', 'can', 'from', 'as', 'be', 'the', 'is', 'are', 'but']
        text_words = self.text.split()
        filtered_words = []
        for word in text_words:
            if word.lower() not in stop_words:
                filtered_words.append(word)           
        return " ".join(filtered_words)
# Create a method called remove_special_characters().
# Use regular expressions to remove special characters from the text attribute.
# Return the modified text.
    def remove_special_characters(self):
        cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', self.text)
        return cleaned_text

text = TextModification("The Sun Is Bright And The Sky Is Blue")
print(text.remove_stop_words())
print(text.word_frequency("sun"))
print(text.most_common_word())
print(text.unique_words())


file_path = os.path.join(dir_path, "words.txt")
print("Looking for file at:", file_path)

text = TextModification.from_file(file_path)
print(text.remove_punctuation())
print(text.remove_stop_words())


