books = {
    "121": {"Title": "Python", "Author": "Anders", "Quantity": 3},
    "122": {"Title": "Hungrig", "Author": "Mikael", "Quantity": 5},
    "123": {"Title": "Bilboken", "Author": "Stefan", "Quantity": 1}
}


def display_books():
    book_list = ""
    for key, value in books.items():
        book_list += f"{key}: {value}\n"
    return book_list


def search_book(isbn_title: str, books: dict) -> str:
    for isbn, book in books.items():
        if isbn_title.lower() in book["Title"].lower() or isbn_title == isbn:
            return f"ISBN: {isbn}. Title: {book['Title']}. Author: {book['Author']}. Quantity: {book['Quantity']}."
    return "Book not found."
    # 
    # isbn_title = input("Type your ISBN number or title: ")
    # isbn_title_match = isbn_title_search(isbn_title)
    # print(isbn_title_match)
    # 


def search_author():
    author = input("Enter your author: ")

    if author in books:
        book = books[author]
        return f"ISBN: {author}. Title: {book['Title']}. Author: {book['Author']}. Quantity: {book['Quantity']}."
    else:
        return f"Book with author {author} not found."


while True:
    print("Welcome to the library!")
    print("1. Show all available books.")
    print("2. Search by title or ISBN.")
    print("3. Search by author.")
    print("4. Add new book to the library.")
    print("5. Update information (search by ISBN).")
    print("6. Delete book from the library (search by ISBN).")
    print("7. ")
    print("8. ")
    print("9. ")
    print("10. ")
    print("11. ")
    print("12. ")
    print("13. ")
    print("14. Exit the program.")
    choice = input("Enter what you would like to do: ")
    if choice == "1":
        print(display_books())
    elif choice == "2":
        print(search_book(isbn_title, books))
    elif choice == "3":
        print(search_author())
    elif choice == "4":
        print()
    elif choice == "5":
        print()
    elif choice == "6":
        print()
    elif choice == "7":
        print()
    elif choice == "8":
        print()
    elif choice == "9":
        print()
    elif choice == "10":
        print()
    elif choice == "11":
        print()
    elif choice == "12":
        print()
    elif choice == "13":
        print()
    elif choice == "14":
        print("Thank you for using this program!")
        exit()
    else:
        print("Bad choice, please try again!")
