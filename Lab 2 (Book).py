class Book:
    def __init__(self, id: int, name: str, pages: int):
        self.id = id
        self.name = name
        self.pages = pages
    def __str__(self):
        return f'Название книги "{self.name}"'

    def __repr__(self):
        return f"Book(id ={self.id}, name='{self.name}', pages={self.pages})"

class Library:
    def __init__(self, books = []):
        self.books = books
    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        else:
            return self.books[-1].id+1
    def get_index_by_book_id(self, id: int):
        for i in self.books:
            if i.id == id:
                return self.books.index(i)
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == "__main__":
    book1 = Book(123456789, "Анна Каренина", 832)
    book2 = Book(123456790, "Война миров", 192)
    Library1 = Library([book1, book2])
    print(Library1.get_next_book_id())
    print(Library1.get_index_by_book_id(123456789))
    #print(Library1.get_index_by_book_id(123456788))
