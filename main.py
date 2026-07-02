from database import SessionLocal
from models import Book
from crud import view_books, add_book

# This method is called from crud.py for viwing books

books = view_books()

for book in books:
    print(book)


book = add_book("Think Python","Allen Downey", "Programming", 750.00, 450, 2, 8)

print(book)