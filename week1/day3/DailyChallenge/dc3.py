#Challenge 1: Letter Index Dictionary
user_word = input('Enter a word:')
letter_indices = {}
for index, letter in enumerate(user_word):
    if letter in letter_indices:
        letter_indices[letter].append(index)
    else:
        letter_indices[letter] = [index]
print(letter_indices)

#Challenge 2: Affordable Items

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

clean_wallet = int(wallet.replace("$", "").replace(",", ""))
print(clean_wallet)

basket = []
for item, price in items_purchase.items():
    clean_price = int(price.replace("$", "").replace(",", ""))
    if clean_wallet >= clean_price:
        basket.append(item)
        clean_wallet -= clean_price
# print(items_purchase)        
# print(clean_price)        
# print(basket)    

if not basket:
    print('Nothing!')
else:    
    print(sorted(basket))
    

