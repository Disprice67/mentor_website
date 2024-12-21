import re


class Slug:
    def __init__(self, value: str):
        if not value or not self._is_valid_slug(value):
            raise ValueError("Slug должен быть непустым и содержать только буквы, цифры и дефисы.")
        self.value = value.strip()

    @staticmethod
    def _is_valid_slug(value: str) -> bool:
        """Проверка, что slug состоит только из букв, цифр и дефисов."""
        return bool(re.match(r'^[a-zA-Z0-9-]+$', value))

    def __str__(self):
        return self.value

    def __eq__(self, other):
        return isinstance(other, Slug) and self.value == other.value

    def __hash__(self):
        return hash(self.value)


class ProfilePicture:
    def __init__(self, image_data: bytes):
        if not image_data:
            raise ValueError("Profile picture не может быть пустым.")
        self.image_data = image_data

    def __eq__(self, other):
        return isinstance(other, ProfilePicture) and self.image_data == other.image_data

    def __hash__(self):
        return hash(self.image_data)


class Title:
    def __init__(self, value: str):
        if not value or len(value) > 50:
            raise ValueError("Title должен быть непустым и не превышать 50 символов.")
        self.value = value.strip()

    def __str__(self):
        return self.value

    def __eq__(self, other):
        return isinstance(other, Title) and self.value == other.value

    def __hash__(self):
        return hash(self.value)


class Color:
    def __init__(self, value: str):
        if not value or len(value) > 20:
            raise ValueError("Color должен быть непустым и не превышать 20 символов.")
        self.value = value.strip()

    def __str__(self):
        return self.value

    def __eq__(self, other):
        return isinstance(other, Color) and self.value == other.value

    def __hash__(self):
        return hash(self.value)