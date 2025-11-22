from game import Game

def get_user_menu_choice():
    print('___Rock, Paper, Scissors___')
    while True:
        print('Menu:\nPlay a game - 1 \nShow scores - 2 \nQuit - 3')
        user_choice = input('Enter your choice(1/2/3):').strip()
        valid_choices = ['1','2','3']
        if user_choice in valid_choices:
            return user_choice
        else:
            print('Invalid input. Choose 1, 2 or 3 ')  

def print_results(results):
    print('\n__Results__')
    print(f'Wins : {results['win']}')
    print(f'Losses : {results['loss']}')
    print(f'Draws : {results['tie']}')
    print('Thank you for playing!')        

def main():
    results = {'win': 0, 'loss': 0, 'tie': 0}
    while True:
        user_choice = get_user_menu_choice()
        if user_choice == '1':
            game1 = Game()
            result = game1.play()
            results[result] +=1
        elif user_choice == '2':
            print_results(results)
        elif user_choice == '3':
            print_results(results)
            break

if __name__ == "__main__":
    main()            
    
