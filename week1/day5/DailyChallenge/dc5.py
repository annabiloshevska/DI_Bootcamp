#Challenge 1: Sorting

user_str = input('Enter a couple words separated by commas:')
word_list = user_str.split(',')
print(word_list)
sorted_list = sorted(word_list)

result = ', '.join(sorted_list)
print(result)
type(result)

#Challenge 2: Longest Word

user_sentence = input('Enter your message:')
result_sentence = user_sentence.split()
print(result_sentence)
def find_longest_word(sentence):
  longest_word = []
  for word in sentence:
    if len(word) > len(longest_word):
      longest_word = word
  print(f'The longest word is:{longest_word}')

find_longest_word(result_sentence)
