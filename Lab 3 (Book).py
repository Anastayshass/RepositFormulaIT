class Book:
    """ Базовый класс книги. """
    def init(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def str(self):
        return f"Книга {self.name}. Автор {self.author}"


class PaperBook(Book):
    def init(self, _name: str, _author: str, pages: int):
        super().init(_name, _author)
        self.pages = None
        self.set_pages(pages)

    def set_pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages # "Количество страниц"

    def str(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    def repr(self):
        return f"{self.class.name}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(PaperBook):
    def init(self, _name: str, _author: str, duration: float):
        super().init(_name, _author)
        self.duration = None
        self.set_duration(duration)

    def set_duration(self, duration: float):
        if not isinstance(duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self.duration = duration # "Продолжительность"

    def str(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"

    def repr(self):
        return f"{self.class.name}(name={self.name!r}, author={self.author!r}, duration={self.duration})"


my_paper_book = PaperBook("Зов ктухлху", "Говард Лавкрафт", 200)
print(my_paper_book.name)
