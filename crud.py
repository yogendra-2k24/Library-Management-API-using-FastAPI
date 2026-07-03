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


def update_book_price(title, new_price):

    session = SessionLocal()

    try:

        book = session.query(Book).filter(
            Book.title == title
        ).first()

        if book:

            book.price = new_price

            session.commit()

            session.refresh(book)

            return book
        
        return None
    
    except Exception:

        session.rollback()

        raise

    finally:

        session.close()


def delete_book(title):

    session = SessionLocal()

    try:

        book = session.query(Book).filter(
            book.title == title
        ).first()

        if book:

            session.delete(book)

            session.commit()

            return True
    
        return False

    except Exception:

        session.rollback()

        raise

    finally:

        session.close()