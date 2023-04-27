from tkinter import *
from book import Book
from tkinter import messagebox
from lib import Library


class LibWindow:
    def __init__(self, window):
        self.window = window
        window.title("Library Management System")

        self.library = Library()

        self.title_label = Label(window, text="Book Name", font=("Arial", 20))
        self.title_label.grid(row=0, column=0, padx=20, pady=10)

        self.title_entry = Entry(window, font=("Arial", 20))
        self.title_entry.grid(row=0, column=1, padx=20, pady=10)

        self.author_label = Label(window, text="Author", font=("Arial", 20))
        self.author_label.grid(row=1, column=0, padx=20, pady=10)

        self.author_entry = Entry(window, font=("Arial", 20))
        self.author_entry.grid(row=1, column=1, padx=20, pady=10)

        self.add_button = Button(window, text="Add Book", font=("Arial", 15), command=self.add_book)
        self.add_button.grid(row=3, column=0, padx=20, pady=10)

        self.remove_button = Button(window, text="Remove Book", font=("Arial", 15), command=self.remove_book)
        self.remove_button.grid(row=3, column=1, padx=20, pady=10)

        self.book_listbox = Listbox(window, font=("Arial", 15), height=10, width=40)
        self.book_listbox.grid(row=4, column=0, columnspan=4, padx=20, pady=10)

        self.update_book_listbox()

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()

        if title and author:
            book = Book(title, author)
            self.library.add_book(book)
            self.update_book_listbox()
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter a title, author")

    def remove_book(self):
        selected_books = self.book_listbox.curselection()
        if selected_books:
            for book_index in selected_books:
                book = self.library.get_books()[book_index]
                self.library.remove_book(book)
            self.update_book_listbox()

    def update_book_listbox(self):
        self.book_listbox.delete(0, END)
        for book in self.library.get_books():
            self.book_listbox.insert(END, str(book))

    def clear_entries(self):
        self.title_entry.delete(0, END)
        self.author_entry.delete(0, END)
