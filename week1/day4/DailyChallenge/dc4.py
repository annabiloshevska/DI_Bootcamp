menu_dict = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}

def show_menu(menu_dict):
    for drink, price in menu_dict.items():
        print(f'{drink} - {price}')


#show_menu(menu_dict)

def add_item(menu_dict):
    new_drink_name = input('Enter a new drink name:')
    if new_drink_name in menu_dict.keys():
        print('Item already exists!')
    else:    
        new_drink_price = input('Enter a new drinks price:')
        menu_dict[new_drink_name] = new_drink_price
        print(f'{new_drink_name} added')
    
    
#add_item(menu_dict)

def update_price(menu_dict):
    drink_to_update = input('What drink you want to update:')
    if drink_to_update in menu_dict.keys():
        new_price = input('Enter the new price:')
        menu_dict[drink_to_update] = new_price    
        print('Price updated!')
    else:
        print('Item not found.')

    
#update_price(menu_dict)        

def delete_item(menu_dict):
    drink_to_delete = input('What drink you want to delete:')
    if drink_to_delete in menu_dict.keys():
        del menu_dict[drink_to_delete]
        print('Item deleted.')
    else:
        print('Item not found.')
     


def show_options():
    print('What would you like to do?\n 1. Show menu\n 2. Add item\n 3. Update price\n 4. Delete item\n 5. Exit')


def run_coffee_shop(menu):
    while True:
        show_options()
        user_choice = int(input('Enter your choice(1-5):')) 
        if user_choice == 1:
            show_menu(menu)
        elif user_choice == 2:
            add_item(menu)
        elif user_choice == 3:
            update_price(menu)
        elif user_choice == 4:
            delete_item(menu)
        elif user_choice == 5:
            print("Goodbye!")
            break
        else:
            print('Invalid choice, try again.')
        
        
    


# Start the program
run_coffee_shop(menu=menu_dict)