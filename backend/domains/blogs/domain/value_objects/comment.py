import datetime


class Content:
    def __init__(self, body: str):
        if not body.strip():
            raise ValueError("Текст комментария не может быть пустым.")
        self.body = body.strip()

    def word_count(self) -> int:
        """Подсчёт слов в комментарии."""
        return len(self.body.split())

    def __str__(self):
        return self.body

    def __eq__(self, other):
        return isinstance(other, Content) and self.body == other.body

    def __hash__(self):
        return hash(self.body)


class Author:
    def __init__(self, user_id: int, username: str):
        if not username.strip():
            raise ValueError("Имя автора не может быть пустым.")
        self.user_id = user_id
        self.username = username.strip()

    def __str__(self):
        return self.username

    def __eq__(self, other):
        return isinstance(other, Author) and self.user_id == other.user_id and self.username == other.username

    def __hash__(self):
        return hash((self.user_id, self.username))


class PublishDate:
    def __init__(self, date: datetime.datetime):
        if not isinstance(date, datetime.datetime):
            raise ValueError("Дата публикации должна быть объектом datetime.")
        if date > datetime.datetime.now():
            raise ValueError("Дата публикации не может быть в будущем.")
        self.date = date

    def __eq__(self, other):
        return isinstance(other, PublishDate) and self.date == other.date

    def __hash__(self):
        return hash(self.date)

    def __str__(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S")