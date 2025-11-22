import random

class Game:
    def __init__(self):
        self.items = ['rock', 'paper', 'scissors']
  
    def get_user_item(self):
        while True:
            user_item = input('Select an item((rock/paper/scissors):').lower().strip()
            if user_item not in self.items:
                print('Invalid input. Choose from options: rock/paper/scissors.')
            return user_item
    
    def get_computer_item(self):
        computer_item = random.choice(self.items)
        return computer_item

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return 'tie'
        elif (user_item == 'rock' and computer_item == 'scissors') or\
             (user_item == 'scissors' and computer_item == 'paper') or\
             (user_item == 'paper' and computer_item == 'rock'):
             return 'win' 
        else:
            return 'loss'
    
    def play(self):
        user = self.get_user_item()
        print(f'Your choice is {user}')
        computer = self.get_computer_item()       
        print(f'Your opponent\'s choice is: {computer}')
        result = self.get_game_result(user,computer)
        if result == 'tie':
            print('Its a tie!')
        elif result == 'win':     
            print('You\'ve  won!')
        else:
            print('You\'ve lost!')
        return result    

