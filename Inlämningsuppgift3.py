from library_crud import *


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


# Program som frågar användaren om input och sedan kallar på rätt funktion.
def main():
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


if __name__ == "__main__":
    main()
