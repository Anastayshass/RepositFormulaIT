class Message:
    """
    Базовый класс для представления сообщения.

    Атрибуты:
        sender_ (str): Отправитель сообщения.
        recipient_ (str): Получатель сообщения.
        __status (str): Статус сообщения (по умолчанию "No").  Это приватный атрибут, т.к. у пользователя не должно быть
        возможности самостоятельно его изменять.

    Ошибки:
        TypeError: Если `sender_` не является строкой.
        ValueError: Если `recipient_` не является строкой.
    """
    def __init__(self, sender_: str, recipient_: str, __status = "No"):
        """
        Инициализирует объект Message.

        Аргументы:
            sender_ (str): Отправитель сообщения.
            recipient_ (str): Получатель сообщения.
            __status (str, optional): Статус сообщения. По умолчанию "No"
        """
        if not isinstance(sender_, str):
            raise TypeError("Ник отправителя должен быть типа str")
        self.sender_ = sender_ # Отправитель

        if not isinstance(recipient_, str):
            raise ValueError("Ник получателя должен быть типа str")
        self.recipient_ = recipient_ # Получатель

    def __str__(self):
        """
        Возвращает строковое представление объекта Message:
            str: Строковое представление объекта Message.
        """
        return f'Отправитель "{self.sender_}", получатель "{self.recipient_}"'

    def __repr__(self):
        """
        Возвращает строковое представление объекта Message для отладки:
            str: Строковое представление объекта Message для отладки.
        """
        return f"Message(sender_={self.sender_}, recipient_='{self.recipient_}')"

    def sent(self):
        """
        Устанавливает статус сообщения как "Sent".
        """
        self.__status = "Sent"

    def read(self):
        """
        Устанавливает статус сообщения как "Read".
        """
        self.__status = "Read"

class Text(Message):
    """
    Класс для представления текстового сообщения, наследуется от класса Message.

    Атрибут:
        text (str): Текст сообщения.
    """
    def __init__(self, sender_: str, recipient_: str, text: str):
        """
        Инициализирует объект Text.

        Аргументы:
            sender_ (str): Отправитель сообщения.
            recipient_ (str): Получатель сообщения.
            text (str): Текст сообщения.
        """
        super().__init__(sender_, recipient_, __status = "No")

        self.text = text # Текстовое сообщение

    def __str__(self):
        """
        Возвращает строковое представление объекта Text:
            str: Строковое представление объекта Text.
        """
        return f'Отправитель "{self.sender_}", получатель "{self.recipient_}". Сообщение "{self.text}"'

    def __repr__(self):
        """
        Возвращает строковое представление объекта Text для отладки:
            str: Строковое представление объекта Text для отладки.
        """
        return f"{self.__class__.__name__}(sender_={self.sender_}, recipient_={self.recipient_}, text={self.text})"

class Voice(Message):
    """
    Класс для представления голосового сообщения, наследуется от класса Message.

    Атрибуты:
        duration (float): Длительность голосового сообщения.
    """
    def __init__(self, sender_: str, recipient_: str, duration: float):
        """
        Инициализирует объект Voice.

        Аргументы:
            sender_ (str): Отправитель сообщения.
            recipient_ (str): Получатель сообщения.
            duration (float): Длительность голосового сообщения.
        """
        super().__init__(sender_, recipient_, __status = "No")

        self.duration = duration # Голосовое сообщение (показана его длительность)

    def listened(self):
        """
        Устанавливает статус голосового сообщения как "Listened".
        """
        self.__status = "Listened"

    def __str__(self):
        """
        Возвращает строковое представление объекта Voice:
            str: Строковое представление объекта Voice.
        """
        return f'Отправитель "{self.sender_}", получатель "{self.recipient_}". Голосовое сообщение "{self.duration}"'

    def __repr__(self):
        """
        Возвращает строковое представление объекта Voice для отладки:
            str: Строковое представление объекта Voice для отладки.
        """
        return (f"{self.__class__.__name__}(sender_={self.sender_}, recipient_={self.recipient_},"
                f" duration={self.duration})")
