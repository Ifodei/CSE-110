print ("Please enter the items at the shopping list. (enter: quit to finish)")

items = []

shopping_list = ""

while shopping_list != "quit":
    shopping_list = input ("What is the shopping list item?")
    if shopping_list != "quit":
        items.append (shopping_list)

print ("The items are:")

for item in items:
    print (item)

print ("Items with indices are:")

for i in range (len(items)):
    shopping = items [i]
    print (f"{i}. {items [i]}")

users_index = int(input("Which item would you like to change?"))
new_item = input ("What is the new item?")

items [users_index] = new_item

print ("The new shopping list with indices:")

for i in range (len(items)):
    shopping = items [i]
    print (f"{i}. {items [i]}")