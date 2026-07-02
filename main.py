from database import SessionLocal
from models import Book

session = SessionLocal()

books = session.query(Book).all()

for book in books:
    print(book)

new_book = Book(
    title="Atomic Habits",
    author="James Clear",
    category="Self Help",
    price=599,
    pages=320,
    edition=1,
    available_copies=5
)

session.add(new_book)

session.commit()