from typing import Optional
import datetime
import re


class Category:
    def __init__(
            self,
            id: Optional[int],
            name: str,
            slug: str,
            created_at: Optional[datetime.datetime],
            is_draft: bool,
    ):
        self.id = id
        self.name = name
        self.slug = slug
        self.created_at = created_at
        self.is_draft = is_draft

    def update_name(self, new_name: str):
        """Обновить имя категории."""
        if not new_name.strip():
            raise ValueError("Имя категории не может быть пустым.")
        self.name = new_name.strip()

    def update_slug(self, new_slug: str):
        """Обновить slug категории."""
        if not self._is_valid_slug(new_slug):
            raise ValueError("Slug содержит недопустимые символы.")
        self.slug = new_slug.strip()

    @staticmethod
    def _is_valid_slug(slug: str) -> bool:
        """Проверить, что slug состоит только из допустимых символов."""
        return bool(re.match(r'^[a-zA-Z0-9-]+$', slug))

    def publish(self):
        """Сделать категорию опубликованной (убрать черновик)."""
        if self.is_draft:
            self.is_draft = False
            if not self.created_at:
                self.created_at = datetime.datetime.now()

    def to_draft(self):
        """Перевести категорию в черновик."""
        self.is_draft = True
        self.created_at = None
