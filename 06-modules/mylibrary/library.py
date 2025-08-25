"""
library.py

Provides a `Library` class to manage books in a simple collection.
Each book is stored as a tuple of (title, author).
"""

from typing import List, Tuple


class Library:
    """
    A class to manage a library's book collection.

    Methods:
        add_book(title, author) -> None
        remove_book(title) -> None
        search_book(title) -> None
        show_books() -> None
    """

    def __init__(self):
        """Initialize an empty list to store books."""
        self.books: List[Tuple[str, str]] = []

    def add_book(self, title: str, author: str) -> None:
        """
        Add a new book to the library.

        Args:
            title (str): The title of the book.
            author (str): The author's name.
        """
        self.books.append((title, author))
        print(f'"{title}" by {author} has been successfully added to the library.')

    def remove_book(self, title: str) -> None:
        """
        Remove a book from the library by title (case-insensitive).

        Args:
            title (str): The title of the book to remove.
        """
        removed = False
        for book in self.books[:]:
            if title.lower() == book[0].lower():
                self.books.remove(book)
                print(
                    f'"{book[0]}" has been successfully removed from the library.')
                removed = True
        if not removed:
            print(f'No book titled "{title}" was found in the library.')

    def search_book(self, title: str) -> None:
        """
        Search for a book by title (case-insensitive).

        Args:
            title (str): The title to search for.
        """
        found = False
        print("Search results:")
        for book in self.books:
            if title.lower() == book[0].lower():
                print(f'– "{book[0]}" by {book[1]}')
                found = True
        if not found:
            print(f'No matches found for "{title}".')

    def show_books(self) -> None:
        """Display all books in the library."""
        if not self.books:
            print("The library is currently empty.")
        else:
            print("Books available in the library:")
            for num, book in enumerate(self.books, start=1):
                print(f'{num}. "{book[0]}" by "{book[1]}"')
