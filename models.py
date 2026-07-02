from sqlalchemy import String, Integer, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column
from decimal import Decimal
from datetime import date

from database import Base

class Book(Base):
    __tablename__ = "books"

    book_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    title: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    
    author: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    category: Mapped[str] = mapped_column(
        String(100)
    )

    price: Mapped[Decimal] = mapped_column(
        DECIMAL(10, 2)
    )

    pages: Mapped[int] = mapped_column(
        Integer
    )

    edition: Mapped[int] = mapped_column(
        Integer
    )

    available_copies: Mapped[int] = mapped_column(
        Integer
    )

    def __repr__(self):
        return f"Book(id={self.book_id}, title='{self.title}', author='{self.author}')"
    
class Member(Base):

    __tablename__ = "members"

    member_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(100),
        unique=True
    )

    phone: Mapped[str] = mapped_column(
        String(15),
    )

    membership_date: Mapped[date]

class IssuedBook(Base):

    __tablename__ = "issued_books"

    issue_id: Mapped[int]

    book_id: Mapped[int]

    member_id: Mapped[int]

    issue_date: Mapped[date]

    return_date: Mapped[date]

    status: Mapped[str]