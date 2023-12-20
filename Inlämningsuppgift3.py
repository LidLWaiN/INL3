books = {
    "121": {"Title": "Python", "Author": "Anders", "Quantity": 3},
    "122": {"Title": "Hungrig", "Author": "Mikael", "Quantity": 5},
    "123": {"Title": "Bilboken", "Author": "Stefan", "Quantity": 1},
    "124": {"Title": "Mopedboken", "Author": "Stefan", "Quantity": 8}
}


# Printar de olika menyvalen.
def menu():
    print("Welcome to the library!")
    print("1. Show all available books.")
    print("2. Search by title or ISBN.")
    print("3. Search by author.")
    print("4. Add new book to the library.")
    print("5. Update information (search by ISBN).")
    print("6. Delete book from the library (search by ISBN).")
    print("7. Exit the program.")


# Funktion som returnerar alla böcker i form av sträng.
def display_books(books: dict) -> str:
    book_list = ""
    for key, value in books.items():
        book_list += f"{key}: {value}\n"
    return book_list


# Funktion som söker efter bok med hjälp av inmatat ISBN eller titel.
def search_book(isbn_title: str, books: dict) -> str:
    for isbn, book in books.items():
        if isbn_title.lower() in book["Title"].lower() or isbn_title == isbn:
            return f"ISBN: {isbn}. Title: {book['Title']}. Author: {book['Author']}. Quantity: {book['Quantity']}.\n"
    return f"Book with {isbn_title} not found.\n"


# Funtion som söker efter böcker från inmatad författare.
def search_author(author: str, books: dict) -> str:
    found_books = []
    for isbn, book in books.items():
        if author.lower() in book["Author"].lower():
            found_books.append(
                f"ISBN: {isbn}. Title: {book['Title']}. Author: {book['Author']}. Quantity: {book['Quantity']}.")
    if found_books:
        return "\n".join(found_books) + "\n"
    else:
        return f"No books found by author {author}.\n"


# Funktion som
def add_book():
    asd


# Funktion som
def update_book():
    asd


# Funktion som
def delete_book():
    asd


# Funktion som
def save_books():
    asd


# Funktion som
def load_books():
    asd


# Program som frågar användaren om input och sedan kallar på rätt funktion.
while True:
    menu()
    choice = input("Enter what you would like to do: ")
    if choice == "1":
        print(display_books(books))
    elif choice == "2":
        isbn_title = input("Type your ISBN number or title: ")
        print(search_book(isbn_title, books))
    elif choice == "3":
        author = input("Enter your author: ")
        print(search_author(author, books))
    elif choice == "4":
        print(add_book)
    elif choice == "5":
        print(update_book)
    elif choice == "6":
        print(delete_book)
    elif choice == "7":
        print("Thank you for using this program!")
        exit()
    else:
        print(f"Bad choice, please try again!\n")

