import re
import datetime


class CategoryName:
    def __init__(self, value: str):
        if not value.strip():
            raise ValueError("Имя категории не может быть пустым.")
        if len(value.strip()) > 100:
            raise ValueError("Имя категории не может быть длиннее 100 символов.")
        self.value = value.strip()

    def __str__(self):
        return self.value

    def __eq__(self, other):
        return isinstance(other, CategoryName) and self.value == other.value

    def __hash__(self):
        return hash(self.value)


class Slug:
    def __init__(self, value: str):
        if not value.strip():
            raise ValueError("Slug не может быть пустым.")
        if not self._is_valid_slug(value):
            raise ValueError("Slug содержит недопустимые символы.")
        self.value = value.strip()

    @staticmethod
    def _is_valid_slug(slug: str) -> bool:
        """Проверить, что slug состоит только из допустимых символов."""
        return bool(re.match(r'^[a-zA-Z0-9-]+$', slug))

    def __str__(self):
        return self.value

    def __eq__(self, other):
        return isinstance(other, Slug) and self.value == other.value

    def __hash__(self):
        return hash(self.value)


class CreationDate:
    def __init__(self, date: datetime):
        if date > datetime.datetime.now():
            raise ValueError("Дата создания не может быть в будущем.")
        self.date = date

    def __str__(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S")

    def __eq__(self, other):
        return isinstance(other, CreationDate) and self.date == other.date

    def __hash__(self):
        return hash(self.date)
