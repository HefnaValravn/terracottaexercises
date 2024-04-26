def find(books, find):
    for book in books:
        if find(book):
            return book
    
    return None