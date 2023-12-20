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


