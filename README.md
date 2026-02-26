# Резюме-портфолио Django-разработчика

Персональный сайт-резюме и портфолио, разработанный на Django. Проект демонстрирует навыки веб-разработки, владение фреймворком, работу с базами данных, кастомизацию админ-панели, деплой и организацию кода. Сайт содержит страницы «Главная», «Обо мне», «Проекты», «Навыки», «Резюме» и «Контакты», а также собственную систему коротких ссылок для отслеживания переходов.

## Возможности

- Управление контентом страниц через админку (модель `Page`) с WYSIWYG-редактором TinyMCE и возможностью загрузки нескольких изображений.
- Карточки проектов с категориями, технологиями (ManyToMany), ссылками на GitHub и демо.
- Страница навыков с группировкой по категориям и уровнями владения (знакомство, начальный, средний, продуктивный).
- Модальное окно для просмотра изображений в полном размере (клик по картинке) с закрытием по Esc/клику вне изображения.
- Сервис коротких ссылок (`shortlinks`) для отслеживания переходов (например, с HH.ru) с подсчётом кликов.
- Адаптивная вёрстка на Bootstrap 5.
- Фиксированная навигационная панель (меню всегда доступно при прокрутке).
- Кнопка «Наверх» для быстрого возврата к началу страницы.
- Панель администратора с удобными фильтрами и сортировкой.

## Технологии

- **Backend:** Python 3.13, Django 5.2, Django REST Framework (используется частично)
- **База данных:** SQLite (разработка), PostgreSQL (продакшн)
- **Фронтенд:** Bootstrap 5, HTML5, CSS3, JavaScript (нативный)
- **Редактор:** django-tinymce
- **Отладка:** django-debug-toolbar, livereload
- **Мониторинг:** Rollbar (интегрирован)
- **Управление зависимостями:** uv (pyproject.toml)
- **Изображения:** Pillow

## Быстрый старт

**Предварительные требования**

- Установленный `Python 3.13+`
- Установленный `uv`

1. Клонируйте репозиторий

```bash
git clone https://github.com/<project>.git
cd project
```

2. Создайте и активируйте виртуальное окружение и установите зависимости:

```bash
uv venv
.\.venv\Scripts\Activate.ps1  # Windows  (PowerShell)
.\.venv\Scripts\activate.bat  # Windows (cmd)
source .venv/bin/activate     # Linux/macOS
uv sync
```

3. Настройка переменных окружения

Создайте файл `.env` в корне проекта:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Опционально: Rollbar
ROLLBAR_ACCESS_TOKEN=your-token
ROLLBAR_ENVIRONMENT=development

# Для PostgreSQL (если используете)
DATABASE_URL=postgres://user:password@localhost:5432/dbname
```

- `SECRET_KEY` - Секретный ключ Django (обязательно сменить в продакшене)
- `DEBUG` - Режим отладки (локально `True`/продакшен `False`)
- `ALLOWED_HOSTS` - Список разрешённых хостов через запятую
- `ROLLBAR_ACCESS_TOKEN` - Токен доступа к Rollbar для мониторинга ошибок (необязательно)
- `ROLLBAR_ENVIRONMENT` - Окружение для Rollbar (`development`, `production` и т.п.) (необязательно)
- `DATABASE_URL` - URL базы данных в формате postgres://... (по умолчанию SQLite) (необязательно)

4. Миграции и запуск

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Сайт будет доступен по адресу http://127.0.0.1:8000, админка — http://127.0.0.1:8000/admin.

## Структура проекта

```text
django-resume/
├── resume_portfolio/               # Основные настройки проекта
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── pages/                          # Управление статическими страницами
│   ├── migrations/
│   ├── templates/pages/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── projects/                       # Проекты (портфолио)
│   ├── migrations/
│   ├── templates/projects/
│   ├── admin.py
│   └── models.py
├── skills/                         # Навыки
│   ├── migrations/
│   ├── admin.py
│   └── models.py
├── shortlinks/                     # Сервис коротких ссылок
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── templates/                      # Общие шаблоны (base.html, index.html)
├── static/                         # Статические файлы (CSS, JS, Bootstrap)
├── media/                          # Загруженные пользователем файлы
├── manage.py
├── pyproject.toml                  # Зависимости (uv)
└── README.md
```

## Особенности реализации

- **Страницы:** модель `Page` с полем `content` (TinyMCE) и связанными изображениями (`PageImage`), возможность сортировки изображений.
- **Проекты:** модель `Project` с категориями (выбор из фиксированного списка), технологиями (через `ManyToManyField`) и ссылками на репозиторий/демо.
- **Навыки:** модель `Skill` с категориями, уровнями и описанием, выводятся сгруппированными на отдельной странице.
- **Короткие ссылки:** приложение `shortlinks` – при переходе по ссылке вида `/go/slug/` увеличивается счётчик кликов, затем идёт редирект.
- **Модальное окно:** кастомный JavaScript, перехватывающий клики по ссылкам на изображения и показывающий их во всплывающем окне с тёмным фоном и крестиком.

## Автор

**Винокурова Ольга**

Python/Django-разработчик

- GitHub: [OlgaVino25](https://github.com/OlgaVino25?tab=repositories)
- Telegram: [@OlgaVino25](https://t.me/OlgaVino25)
- Email: [olgavinokyrova25@yandex.ru](mailto:olgavinokyrova25@yandex.ru)

## Лицензия

Проект распространяется под лицензией MIT. Подробнее см. файл [LICENSE](LICENSE).
