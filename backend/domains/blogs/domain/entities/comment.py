from typing import Optional
import datetime


class Comment:
    def __init__(
            self,
            id: Optional[int],
            article: 'Article',
            author: 'Author',
            content: str,
            created_at: datetime,
            is_draft: bool,
            likes_count: int,
            dislikes_count: int,
            views_count: int,
    ):
        self.id = id
        self.article = article
        self.author = author
        self.content = content
        self.created_at = created_at
        self.is_draft = is_draft
        self.likes_count = likes_count
        self.dislikes_count = dislikes_count
        self.views_count = views_count

    def update_content(self, new_content: str):
        """Обновить контент статьи."""
        self.content = new_content

    def increment_views(self):
        """Увеличить количество просмотров."""
        self.views_count += 1

    def increment_likes(self):
        """Увеличить количество лайков."""
        self.likes_count += 1

    def increment_dislikes(self):
        """Увеличить количество дизлайков."""
        self.dislikes_count += 1

    def update_author(self, new_author: 'Author'):
        """Обновить автора статьи."""
        self.author = new_author

    def update_article(self, new_article: 'Article'):
        """Обновить статью."""
        self.article = new_article

    def publish(self):
        """Опубликовать комментарий (убрать черновик)."""
        # В Figma для комментария, можно выбрать дату, по-моему это некорректно
        if self.is_draft:
            self.is_draft = False
            if not self.created_at:
                self.created_at = datetime.datetime.now()
