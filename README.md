# Сайт Ментора 🚀

Добро пожаловать в проект **Сайт Ментора**! 🎉 Этот проект направлен на создание удобной платформы для наставничества, где пользователи могут делиться знаниями, искать ментора, а также взаимодействовать с различными материалами и статьями.

## Технологии 🛠️

- **Django** и **Python** — для серверной части и обработки данных.
- **React** и **JavaScript** — для динамичного интерфейса пользователя.
- **Nginx** — для эффективного управления серверными запросами.
- **Docker** — для контейнеризации приложения и его развертывания в любых средах.

## Функционал 🌟

Проект включает следующие ключевые функции:

- **Главная страница** с лендингом.
- **Блог** с возможностью поиска и фильтрации статей.
- **Просмотр статей в формате Markdown**.
- **Комментарии** для взаимодействия с контентом.
- **Админка** для управления пользователями и статьями.

## Установка Backend📦

Для того чтобы запустить проект локально, следуйте этим шагам:

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/mentor_website/mentor-site.git
2. **Установите Poetry:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
3. **Создайте виртуальное окружение и установите зависимости:
   ```bash
   poetry install
4. **Активируйте виртуальное окружение:
   ```bash
   poetry shell
5. **Запустите сервер:
   ```bash
   python manage.py runserver

## Установка Frontend📦
1. **Скачайте и установите [Node.js](https://nodejs.org/en/download/package-manager)**:

2. **В термниале перейдите в папку Frontend**:
   ```bash
   cd /frontend
3. **Установите зависимости:
   ```bash
   npm install
4. **Запустите frontend:
   ```bash
   npm start


## Использование pre-commit 🛠️
Мы используем pre-commit для автоматической проверки кода перед каждым коммитом. Это помогает поддерживать качество кода и соответствие стандартам.

## Дополнительно 📚
Обязательно ознакомьтесь с файлом CONTRIBUTING.md для получения дополнительной информации о правилах и процессах внесения изменений в проект.

Помечайте закрытый PR лейблом!!!

Спасибо за вклад в проект! 🎈
