import datetime


class Slug:
    def __init__(self, value: str):
        if not value:
            raise ValueError('Slug не определен')
        self.value = value

    def __str__(self):
        return self.value

    def __eq__(self, other):
        return isinstance(other, Slug) and self.value == other.value

    def __hash__(self):
        return hash(self.value)


class ProfilePicture:
    def __init__(self, image_data: bytes):
        if not image_data:
            raise ValueError('Image не определен')
        self.image_data = image_data

    def __eq__(self, other):
        return isinstance(other, ProfilePicture) and self.image_data == other.image_data

    def __hash__(self):
        return hash(self.image_data)


class Content:
    def __init__(self, body: str):
        if not body:
            raise ValueError("Content не определен")
        self.body = body

    def word_count(self) -> int:
        """Подсчёт слов в статье."""
        return len(self.body.split())

    def __str__(self):
        return self.body

    def __eq__(self, other):
        return isinstance(other, Content) and self.body == other.body

    def __hash__(self):
        return hash(self.body)


class Title:
    def __init__(self, value: str):
        if not value or len(value) > 200:
            raise ValueError("Title не определен или больше 200 символов.")
        self.value = value.strip().title()

    def __str__(self):
        return self.value

    def __eq__(self, other):
        return isinstance(other, Title) and self.value == other.value

    def __hash__(self):
        return hash(self.value)


class PublishDate:
    def __init__(self, date: datetime):
        if not isinstance(date, datetime):
            raise ValueError("Publish date не datetime объект")
        self.date = date

    def __eq__(self, other):
        return isinstance(other, PublishDate) and self.date == other.date

    def __hash__(self):
        return hash(self.date)

    def __str__(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S")
