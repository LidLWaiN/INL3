books = {
    "121": {"Title": "Python", "Author": "Anders", "Quantity": 3},
    "122": {"Title": "Hungrig", "Author": "Mikael", "Quantity": 5},
    "123": {"Title": "Bilboken", "Author": "Stefan", "Quantity": 1},
    "124": {"Title": "Mopedboken", "Author": "Stefan", "Quantity": 8}
}


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


# Funtion som söker efter böcker med hjälp av inmatad författare.
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


# def add_book():
#
#
#
# def update_book():
#
#
#
# def delete_book():
#
