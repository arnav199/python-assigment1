

import sys
from library_manager.inventory import LibraryInventory

def get_input(prompt):
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye")
        sys.exit(0)

def print_books(books):
    if not books:
        print("No books found.")
        return
    for b in books:
        print("-", b)

def main():
    inv = LibraryInventory() 

    while True:
        print("\nLibrary Inventory Manager")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search by Title")
        print("6. Search by ISBN")
        print("7. Exit")
        choice = get_input("Enter choice (1-7): ").strip()

        if choice == "1":
            title = get_input("Title: ").strip()
            author = get_input("Author: ").strip()
            isbn = get_input("ISBN: ").strip()
            try:
                b = inv.add_book(title, author, isbn)
                print("Added:", b)
            except Exception as e:
                print("Error:", e)

        elif choice == "2":
            isbn = get_input("ISBN to issue: ").strip()
            try:
                b = inv.issue_book(isbn)
                print("Issued:", b)
            except Exception as e:
                print("Error:", e)

        elif choice == "3":
            isbn = get_input("ISBN to return: ").strip()
            try:
                b = inv.return_book(isbn)
                print("Returned:", b)
            except Exception as e:
                print("Error:", e)

        elif choice == "4":
            books = inv.display_all()
            print_books(books)

        elif choice == "5":
            q = get_input("Title search: ").strip()
            results = inv.search_by_title(q)
            print_books(results)

        elif choice == "6":
            isbn = get_input("ISBN search: ").strip()
            book = inv.search_by_isbn(isbn)
            if book:
                print(book)
            else:
                print("Not found.")

        elif choice == "7":
            print("Goodbye.")
            break

        else:
            print("Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()

