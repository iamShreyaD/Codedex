
def welcome():
    print("1. 🍔 Cheeseburger")
    print("2. 🍟 Fries")
    print("3. 🥤 Soda")
    print("4. 🍦 Ice Cream")
    print("5. 🍪 Cookie")

welcome()


item_number = int(input("Enter the number of the item you want to order: "))

def get_item(item_number):
    if item_number == 1:
        item_name = '🍔 Cheeseburger'

    elif item_number == 2:
        item_name = '🍟 Fries'

    elif item_number == 3:
        item_name = '🥤 Soda'

    elif item_number == 4:
        item_name = '🍦 Ice Cream'

    elif item_number == 5:
        item_name = '🍪 Cookie'

    else:
        item_name = 'Your item is not on the menu. Try a different item number.'

    return item_name
    
print(get_item(item_number))
  

    
