def add_books(books):
    n = int(input("How many books to add: "))
    for i in range(n):
        b = input("Enter book name: ")
        books.append(b)
    return books
def issue_book(books):
    b = input("Enter book to issue: ")
    if b in books:
        books.remove(b)
        print("Book issued")
    else:
        print("Book not found")
    return books
def return_book(books):
    b = input("Enter book to return: ")
    books.append(b)
    return books
def search_book(books):
    b = input("Enter book to search: ")
    if b in books:
        print("Book available")
    else:
        print("Book not available")

books = []

while True:
    print("1.Add Books")
    print("2.Issue Book")
    print("3.Return Book")
    print("4.Search Book")
    print("5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        books = add_books(books)
    elif ch == 2:
        books = issue_book(books)
    elif ch == 3:
        books = return_book(books)
    elif ch == 4:
        search_book(books)
    elif ch == 5:
        break
    else:
        print("Invalid choice")