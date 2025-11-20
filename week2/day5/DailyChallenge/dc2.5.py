
# Exercise 2: Create a deck of cards class
# The Deck of cards class should NOT inherit from a Card class.

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.
import random
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __str__(self):
        return f'{self.value} of {self.suit}'    

class Deck:
    def __init__(self):
        self.cards = []
        self.shuffle() 

    def shuffle(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = []
        for suit in suits:
            for value in values:
                card = Card(suit,value)
                self.cards.append(card)             
        random.shuffle(self.cards)
    
    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

deck = Deck()
print(deck.deal())         
print(len(deck.cards))    
print(deck.deal())  
print(deck.deal())  
print(deck.deal())  
print(len(deck.cards))  