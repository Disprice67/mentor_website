class Tag:
    def __init__(
        self,
        id: int,
        slug: str,
        profile_picture: bytes,
        title: str,
        color: str,
    ):
        self.id = id
        self.slug = slug
        self.profile_picture = profile_picture
        self.title = title
        self.color = color

    def update_title(self, new_title: str):
        """Обновить название тега."""
        if not new_title.strip():
            raise ValueError("Название тега не может быть пустым.")
        self.title = new_title.strip()

    def update_slug(self, new_slug: str):
        """Обновить slug тега."""
        if not new_slug.strip():
            raise ValueError("Slug не может быть пустым.")
        self.slug = new_slug.strip()

    def update_color(self, new_color: str):
        """Обновить цвет тега."""
        if not new_color.strip():
            raise ValueError("Цвет не может быть пустым.")
        self.color = new_color.strip()

    def update_profile_picture(self, new_picture: bytes):
        """Обновить картинку тега."""
        if not new_picture:
            raise ValueError("Изображение не может быть пустым.")
        self.profile_picture = new_picture
