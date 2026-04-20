#books = ["Dreams from My Father", "Gifted Hands", "Who Moved my Cheese" ]

#books.append ("Dreams from My Father")
#books.append ("Gifted Hands")
#books.append ("Who Moved my Cheese")
#print (books)
#print ("Your books are:")
#for book in books:
#    print (book)
friends = []

new_friend = None

while new_friend != "end":
    new_friend = input ("What is the name of your friend?")
    if new_friend != "end":
        friends.append (new_friend)

print ("Your friends are:")          
for friend in friends:
    print (friend)
