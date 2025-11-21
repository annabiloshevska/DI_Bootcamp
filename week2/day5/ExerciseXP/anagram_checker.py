#Anagram Checker
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
  
class AnagramChecker:
    # def __init__(self):
    #     with open(dir_path + '\sowpods.txt', 'r') as f:
    #         words = f.read().lower().split()
    #         self.words = set(words)
    #     #print(words)
    def __init__(self):
        path = os.path.join(dir_path, "sowpods.txt")
        with open(path, "r", encoding="utf-8") as f:
            words = f.read().lower().split()
            self.words = set(words)
    


    def is_valid_word(self, word):
        word = word.lower()
        if word in self.words:
            return True
        else: 
            return False
        
    def is_anagram(self, word1, word2):
        word1 = word1.lower().strip(' ')
        word2 = word2.lower().strip(' ')
        if word1 == word2:
            return False
        sorted1 = sorted(word1) 
        sorted2 = sorted(word2)
        if sorted1 == sorted2:
            return True
        else:
            return False
   
    def get_anagrams(self, word):
        word = word.lower()
        anagrams = []
        for item in self.words:
            if self.is_anagram(word,item):
                anagrams.append(item)
        return set(anagrams)

        

    

        