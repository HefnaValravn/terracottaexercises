import pytest
from book import Book


@pytest.mark.parametrize('title', [
    'asdf',
    'wfr',
    'brother',
    'amazing'
])
@pytest.mark.parametrize('isbn', [
    '9780141439563',
    '9780141439563',
    '978-0-596-52068-7'
])

def test_valid_creation(title, isbn):
    book = Book(title, isbn)
    assert book.title == title
    assert book.isbn == isbn
    
    
    
@pytest.mark.parametrize('title', [
    '',
    '',
    '',
    ''
])
@pytest.mark.parametrize('isbn', [
    '9780141439563',
    '9780141439563',
    '978-0-596-52068-7'
])
def test_creation_with_invalid_title(title, isbn):
    with pytest.raises(RuntimeError):
        book = Book(title, isbn)
        
        
        
@pytest.mark.parametrize('title', [
    'asdf',
    'wfr',
    'brother',
    'amazing'
])
@pytest.mark.parametrize('isbn', [
    '978014142343563',
    '9780141439562343',
    '978-0-596-52062348-7'
])
def test_creation_with_invalid_isbn(title, isbn):
    with pytest.raises(RuntimeError):
        book = Book(title, isbn)