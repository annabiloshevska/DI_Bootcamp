from anagram_checker import AnagramChecker

checker = AnagramChecker()

while True:
    print("___Anagram Checker___")
    word = input('Enter a word (or type "exit" to quit):').strip()
    
    if word.lower() == "exit":
        print("Goodbye!")
        break
    
    if len(word.split()) != 1:
            print("Enter just one word")
            continue
    if  not word.isalpha():
        print('Enter just alphabetic characters')
        continue     
    if checker.is_valid_word(word):
        print(f'You have entered a valid word\nYour word is {word}')
        options = checker.get_anagrams(word)
        if options:
            print(f'Anagrams found:',', '.join(options))
        else:
            print('No anagrams found')    
    else:
        print("Sorry, that's not a valid English word")
  