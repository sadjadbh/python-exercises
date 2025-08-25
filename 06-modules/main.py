"""
main.py

Runs a command-line interface for interacting with the Library system.
"""

import sys
from mylibrary.library import Library


def lib_menu(library: Library) -> None:
    """
    Show the interactive library menu.

    Args:
        library (Library): An instance of the Library class.
    """
    while True:
        print("\n📚 Welcome to the Library System 📚")
        print("How can I assist you today?")
        print("1. View all books")
        print("2. Add a new book")
        print("3. Remove a book")
        print("4. Search for a book")
        print("5. Exit")

        ans = input("👉 Please enter your choice (1–5): ").strip()
        print()

        if ans == '1':
            library.show_books()

        elif ans == '2':
            add_title = input("📖 Enter the book title: ").strip().title()
            add_author = input("✍️ Enter the author's name: ").strip().title()
            print()
            library.add_book(add_title, add_author)

        elif ans == '3':
            rem_title = input(
                "🗑️ Enter the title of the book to remove: ").strip()
            print()
            library.remove_book(rem_title)

        elif ans == '4':
            src_title = input("🔎 Enter the title to search for: ").strip()
            library.search_book(src_title)

        elif ans == '5':
            sys.exit("\n👋 Thank you for using the Library System. Goodbye!\n")

        else:
            print("❌ Invalid choice. Please select a number from 1 to 5.")

        input('\n🔁 Press Enter to return to the main menu...')


if __name__ == "__main__":
    lib = Library()
    lib_menu(lib)
