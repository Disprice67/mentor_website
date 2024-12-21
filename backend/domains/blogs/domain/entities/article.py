import datetime
from typing import Optional
import re


class Article:
    def __init__(
            self,
            id: Optional[int],
            title: str,
            profile_picture: bytes,
            content: str,
            created_at: Optional[datetime],
            views_count: int,
            likes_count: int,
            dislikes_count: int,
            is_draft: bool,
            slug: 'Slug',
            author: 'Author',
            category: 'Category',
            comments: list['Comment']
    ):
        self.id = id
        self.title = title
        self.content = content
        self.profile_picture = profile_picture
        self.created_at = created_at
        self.views_count = views_count
        self.likes_count = likes_count
        self.dislikes_count = dislikes_count
        self.is_draft = is_draft
        self.slug = slug
        self.author = author
        self.category = category
        self.comments = comments if comments else []

    def update_content(self, new_content: str):
        """Обновить контент статьи."""
        self.content = new_content

    def update_title(self, new_title: str):
        """Обновить заголов статьи."""
        self.title = new_title

    def update_picture(self, new_picture: bytes):
        """Обвиноть изображение."""
        self.profile_picture = new_picture

    def update_category(self, new_category: 'Category'):
        """Обновить категорию статьи."""
        self.category = new_category

    def update_author(self, new_author: 'Author'):
        """Обновить автора статьи."""
        self.author = new_author

    def increment_views(self):
        """Увеличить количество просмотров."""
        self.views_count += 1

    def increment_likes(self):
        """Увеличить количество лайков."""
        self.likes_count += 1

    def increment_dislikes(self):
        """Увеличить количество дизлайков."""
        self.dislikes_count += 1

    def publish(self):
        """Опубликовать статью (убрать черновик)."""
        if self.is_draft:
            self.is_draft = False
            if not self.created_at:
                self.created_at = datetime.datetime.now()

    def update_slug(self, new_slug: str):
        """Обновить slug категории."""
        if not self._is_valid_slug(new_slug):
            raise ValueError("Slug содержит недопустимые символы.")
        self.slug = new_slug.strip()

    @staticmethod
    def _is_valid_slug(slug: str) -> bool:
        """Проверить, что slug состоит только из допустимых символов."""
        return bool(re.match(r'^[a-zA-Z0-9-]+$', slug))

    def to_druft(self):
        """Убрать статью в черновик."""
        self.is_draft = True
        self.created_at = None

    def add_comment(self, new_comment: 'Comment'):
        """Добавить новый комментарий к статье."""
        self.comments.append(new_comment)

    def remove_comment(self, comment: 'Comment'):
        """Удалить комментарий к статье."""
        if comment in self.comments:
            self.comments.remove(comment)

    def is_author(self, user: 'User') -> bool:
        """Проверить, является ли данный пользователь автором статьи."""
        return self.author.id == user.id
