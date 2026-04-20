first_no= float(input("What is the first number?"))
second_no= float(input("What is the second number?"))

if first_no > second_no:
    print("The first number is greater")
else:
    print("The first number is not greater")

if first_no == second_no:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

if second_no > first_no:
    print("The second number is grater")
else:
    print("The second number is not greater")

print()
favorite_meal= str(input("What is your favorite meal?"))
if favorite_meal.lower() == "cow":
    print("That is my favorite meal too")
else:
    print("That is not my favorite meal")