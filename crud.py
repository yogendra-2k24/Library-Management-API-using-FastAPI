from database import SessionLocal
from models import Book

def view_books():

    session = SessionLocal()

    try:

        books = session.query(Book).all()

        return books

    finally:

        session.close()


def add_book(title, author, category, price, pages, edition, available_copies):

    session = SessionLocal()

    try:
        new_book = Book(
            title = title,
            author = author,
            category = category,
            price = price,
            pages = pages,
            edition = edition,
            available_copies = available_copies
        )

        session.add(new_book)

        session.commit()

        session.refresh(new_book)

        return new_book
    
    finally:

        session.close()


