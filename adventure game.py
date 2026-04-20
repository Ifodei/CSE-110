# The adventure game was played and enjoyed by my wife and nephew. They suggested additions of several 
#scenarios and outcomes such as the CAR YARD as they are into video games pertainig such. They are eager for me
#to go pro and customize games just for them.

print("Welcome to the adventure Game! ")
print("A poker master presents you with three decks of cards. Which deck will you pick? ")
print("FIRST/ SECOND/ THIRD")
choice = input(" Your choice is:").upper()
print()

#def choice a () :
if choice  == "FIRST" :
    print("You chose the FIRST deck.")   
    choice_1 = input(" You are hereby requested to pick one of the two cards : K HEARTS /Q SPADES. Your choice is :").upper()
    if choice_1 == "K HEARTS" :
        print("You chose K HEARTS") 
        choice_2 = input("You are offered a KEY/ a CHEST. You have picked :").upper()
        if choice_2 =="KEY" :
            print("You become KING!")
        elif choice_2 == "CHEST" :
            print("You get TRAPPED in the basement!")
    elif choice_1 == "Q SPADES" :
        print("Sorry, you are now a slave")
else :
    print("Invalid input, GAME OVER!")

print()

#def choice b () :
if choice == "SECOND" :
    print("You chose the SECOND deck")
    choice_3 = input("At this stage, you are required to choose between two doors : RED/ GREEN. Your choice is :").upper()
    if choice_3 == "RED" :
        print("You chose RED")
        choice_4 = input("Now you are presented with two places to choose from : A MAZE/ A DUNGEON : You have picked :").upper()
        if choice_4 == "A MAZE" :
            print("You find your way home")
        elif choice_4 == "A DUNGEON" :
            print("You live with an ORGE")
    elif choice_3 == "GREEN" :
        print("You chose GREEN")
        choice_5 = input("You are presented with a twin staircase. Which flight do you pick RIGHT/ LEFT. Your choice is :").upper()
        if choice_5 == "RIGHT" :
            print("Oops! You have eached a DEAD END!")
        elif choice_5 == "LEFT" :
            print("You've reached the INFINITY HALL")
else:
    print("Invalid input, FALLS INTO THE ABYSS!")

print()
#def choice c () :
if choice == "THIRD" :
    print("You chose the THIRD deck")
    choice_6 = input("You are required to pick which establishment to visit : A MALL/ CAR YARD/ ZOO. Your choice is :").upper()
    if choice_6 == "A MALL" :
        print("You picked A MALL")
        choice_7 = input("Which shop will you visit at the mall : CAFETERIA/ MOVIE THEATRE. Your choice :").upper()
        if choice_7 == "CAFETERIA" :
            print(" You get a DESSERT!")
        elif choice_7 == "MOVIE THEATRE" :
            print("Oops! You meet a SERIAL KILLER!")
    elif choice_6 == "CAR YARD" :
        print(" You picked the CAR YARD")
        choice_8 = input("You arrived at the car yard and find it under attack. What do you do? OPEN FIRE/ RUN. Your choice is :").upper()
        if choice_8 == "OPEN FIRE" :
            print("Sorry, you are SHOT DEAD!")
        elif choice_8 == "RUN" :
            print("You find a ride to TOWN")
    elif choice_6 == "ZOO" :
        print("You picked the ZOO")
        choice_9 = input("Which animal do you want to feed? a LION/ GIRAFFE. Your choice is :").upper()
        if choice_9 == "LION" :
            print("Lion bites your hand")
        elif choice_9 == "GIRAFFE" :
            print("Congratulations! You get FREE TICKETS to the animal Zoo ")
else :
    print("Invalid user. ENTER A VALID OPTION!")




        





