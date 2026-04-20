

with open ("books.txt") as books_file:
    #books_file = books_file.strip()
    for books in  books_file:
        print (books.strip())