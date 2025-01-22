from typing import Optional

class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = pages
    def __str__(self):
        return f'Название книги "{self.name}"'
    def __repr__(self):
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"

class Library:
    def __init__(self, books: Optional[list[Book]] = None):
        if books is None:
            books = []
        self.books = books
    def get_next_book_id(self) -> int:
        if not self.books:
            return 1
        last_book = self.books[-1]
        next_id = last_book.id_ + 1
        return next_id
    def get_index_by_book_id(self, id_: int) -> int:
        for index, book in enumerate(self.books):
            if book.id_ == id_:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == "__main__":
    book1 = Book(123456789, "Анна Каренина", 832)
    book2 = Book(123456790, "Война миров", 192)
    Library1 = Library([book1, book2])
    print(Library1.get_next_book_id())
    print(Library1.get_index_by_book_id(123456789))
    #print(Library1.get_index_by_book_id(123456788))
