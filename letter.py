favorite_letter = input ("What is your favorite letter?")
word = "commitment"

for letter in word:
    if favorite_letter.lower() == letter.lower():
        print (letter.upper(), end="")
    else:
        print (letter.lower(), end="")

#for letter in word:
#    if favorite_letter.lower() == letter.lower():
#        print("_", end="")
#    else:
#        print (letter.lower(), end="")