# I defined the  display menu and its choices for an easier approach and a neater look. This ensures I don't 
#forget any instructions. I also added the break command after option "5" to dismiss the program loop.
print(" Welcome to your shopping cart!")

#Since this is the first/main loop, we define it as it should appear using the "print" function. It also goes 
#before the choice options when starting the while loop.

def display_menu() :
    print(" Please select one of the following :")
    print("1. Add Item ")
    print("2. View Cart ")
    print("3. Remove Item ")
    print("4. Compute Total")
    print("5. Quit")

#Choice "1" defined as per output instructions.
def add_item(shopping_cart, price) :
    item_name = input("What item would you like to add?")
    item_price = float(input(f"The price of {item_name} is :"))
    shopping_cart.append(item_name)
    price.append(item_price)
    print(f" {item_name} has been added to the cart.")


#choice "2" defined.Enumerate and Zip functions are used within the view_cart function to iterate over the 
#items in the shopping cart and their corresponding prices simultaneously, and to print them with a numbered 
#list.
def view_cart(shopping_cart, prices) :
    if not shopping_cart :
        print("The shopping cart is empty")
    else :
        print("The contents in your shopping cart are :") 
        for i, (item_name, item_price) in enumerate(zip(shopping_cart, prices), start = 1 ) :
            print(f"{i}. {item_name} - ${item_price:.2f}")


#Choice "3" defined. Both the item and price eliminated from list and index moves one step backwards.
def remove_item(shopping_cart, prices ) :
    view_cart(shopping_cart, prices)
    item_number = int(input("Which item would you like to remove?"))
    if 1 <= item_number <= len(shopping_cart) :
        removed_item = shopping_cart.pop(item_number -1)
        removed_price = prices.pop(item_number -1)
        print("item has been removed from the shopping cart.")

  #N/B all choices define the lists shopping cart and prices.In the provided code, the functions 
  #need access to the shopping_cart and prices lists in order to perform their respective tasks. Each function 
  #manipulates or displays information from these lists to reflect 
  #the current state of the shopping cart.        
shopping_cart = [] 
prices = []
total_sum = ""

while True :
    display_menu()
    choice = input("Please enter an action :")
    if choice == "1" :
        add_item(shopping_cart, prices)
    elif choice == "2" :
        view_cart(shopping_cart, prices)
    elif choice == "3" :
        remove_item(shopping_cart, prices)
    elif choice == "4" :
        total_sum = sum(prices) 
        print(f"The total price of the items in the shopping cart is : {total_sum:.2f}")
    elif choice == "5" :
        print("Thank you. Goodbye!")
        break
    else :
        print("Invalid choice. Please try again.")

    