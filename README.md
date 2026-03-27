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
- Кнопка «Вверх» для быстрого возврата к началу страницы.
- Панель администратора с удобными фильтрами и сортировкой.

## Технологии

- **Backend:** Python 3.13, Django 5.2, Django REST Framework (используется частично)
- **База данных:** SQLite (разработка), PostgreSQL (продакшн)
- **Фронтенд:** Bootstrap 5, HTML5, CSS3, JavaScript (нативный)
- **Редактор:** django-tinymce
- **Отладка:** django-debug-toolbar, livereload
- **Мониторинг:** Rollbar (интегрирован)
- **Управление зависимостями:** uv (pyproject.toml) + requirements.txt (для Docker)
- **Изображения:** Pillow
- **Контейнеризация:** Docker, Docker Compose

## Быстрый старт (без Docker)

**Предварительные требования**

- Установленный `Python 3.13+`
- Установленный `uv`

1. Клонируйте репозиторий

```bash
git clone https://github.com/OlgaVino25/django-resume.git
cd django-resume
```

2. Создайте и активируйте виртуальное окружение и установите зависимости:

```bash
uv venv
.\.venv\Scripts\Activate.ps1  # Windows  (PowerShell)
.\.venv\Scripts\activate.bat  # Windows (cmd)
source .venv/bin/activate     # Linux/macOS
uv sync                       # установка зависимостей
```

3. Настройка переменных окружения

Создайте файл `.env` в корне проекта:

```env
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Опционально: Rollbar
ROLLBAR_ACCESS_TOKEN=your_token
ROLLBAR_ENVIRONMENT=development

# Для PostgreSQL (если используете)
DATABASE_URL=postgres://user:password@localhost:5432/dbname
```

- `SECRET_KEY` - Секретный ключ Django (обязательно сменить в продакшене)
- `DEBUG` - Режим отладки (локально `True`/продакшен `False`)
- `ALLOWED_HOSTS` - Список разрешённых хостов через запятую без пробелов
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

## Запуск в Docker (режим разработки)

Проект полностью контейнеризирован. Для локальной разработки используется файл `docker-compose.yml`.

1. Убедитесь, что у вас установлены [Docker](https://docs.docker.com/get-started/get-docker/) и [Docker Compose](https://docs.docker.com/compose/install/).
2. Клонируйте репозиторий и перейдите в папку проекта:

```bash
git clone https://github.com/OlgaVino25/django-resume.git
cd django-resume
```

3. Создайте файл `.env` и заполните его своими данными:

```env
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,<your_IP_server>,<your_domain>

DB_NAME=resume_db
DB_USER=postgres
DB_PASSWORD=your_password

ROLLBAR_ACCESS_TOKEN=your_token
ROLLBAR_ENVIRONMENT=development

CSRF_TRUSTED_ORIGINS=https://<your_domain>
CSRF_COOKIE_SECURE=True
SESSION_COOKIE_SECURE=True
```

Важно: для Docker строка `DATABASE_URL` в `.env` не нужна – она формируется в `docker-compose.yml`.

4. Запустите контейнеры:

```bash
docker-compose up --build
```

Сайт станет доступен по адресу `http://localhost:8080` (порт по умолчанию; его можно изменить в `docker-compose.yml`).

5. В другом терминале примените миграции и создайте суперпользователя:

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

6. Загрузите фикстуры, если есть:

```bash
docker-compose exec web python manage.py loaddata data.json
```

Остановка: `Ctrl+C`, затем `docker-compose down`. Для полной очистки (включая тома) используйте `docker-compose down -v`.

# Развёртывание на сервере с Docker (production)

Для продакшена используется `docker-compose.prod.yml`, а в качестве веб-сервера выступает системный Nginx с SSL.

## Подготовка сервера

1. Установите Docker и Docker Compose на сервер (Selectel, Yandex Cloud и т.п.).
2. Клонируйте репозиторий в `/opt/resume`:

```bash
git clone https://github.com/OlgaVino25/django-resume.git /opt/resume
cd /opt/resume
```

3. Создайте файл .env и заполните его продакшен-настройками:

```env
SECRET_KEY=your_secret_key_here
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,<your_IP_server>,<your_domain>

DB_NAME=resume_db
DB_USER=postgres
DB_PASSWORD=your_password

ROLLBAR_ACCESS_TOKEN=your_token
ROLLBAR_ENVIRONMENT=production

CSRF_TRUSTED_ORIGINS=https://<your_domain>
CSRF_COOKIE_SECURE=True
SESSION_COOKIE_SECURE=True
```

Важно: строка `DATABASE_URL` в `.env` не нужна – она задаётся в `docker-compose.prod.yml`.

4. Запустите деплойный скрипт (предварительно сделайте его исполняемым):

```bash
chmod +x deploy.sh
./deploy.sh
```

Скрипт выполнит:

- `git pull` для обновления кода
- остановку старых контейнеров
- пересборку и запуск новых контейнеров (`db` и `web`)
- применение миграций
- сборку статики и копирование её на хост (для `Nginx`)

## Настройка системного Nginx и SSL

1. Установите Nginx на сервер:

```bash
apt update && apt install nginx -y
```

2. Создайте конфигурацию для вашего домена (замените your_domain.com на ваш домен):

```bash
nano /etc/nginx/sites-available/your_domain.com
```

Пример конфигурации:

```nginx
server {
    listen 80;
    server_name your_domain.com www.your_domain.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name your_domain.com www.your_domain.com;

    ssl_certificate /etc/letsencrypt/live/your_domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your_domain.com/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location /static/ {
        alias /opt/resume/staticfiles/;
    }

    location /media/ {
        alias /opt/resume/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

3. Включите сайт и отключите стандартный:

```bash
ln -s /etc/nginx/sites-available/your_domain.com /etc/nginx/sites-enabled/
rm /etc/nginx/sites-enabled/default
nginx -t && systemctl reload nginx
```

4. Получите SSL-сертификат через Certbot:

```bash
apt install certbot python3-certbot-nginx -y
certbot --nginx -d your_domain.com -d www.your_domain.com
```

Следуйте инструкциям. Certbot автоматически настроит HTTPS и обновление сертификатов.

5. Проверьте автообновление:

```bash
systemctl status certbot.timer
certbot renew --dry-run
```

## Обеспечение сохранности медиа-файлов

Медиа-файлы хранятся в томе Docker. В deploy.sh уже добавлено копирование медиа на хост, поэтому при обычном деплое они не теряются. Если вы вносите изменения вручную, можно повторить команду:

```bash
mkdir -p /opt/resume/media
docker cp $(docker-compose -f docker-compose.prod.yml ps -q web):/app/media/. /opt/resume/media/
chmod -R 755 /opt/resume/media
```

Для автоматизации можно добавить эту команду в `deploy.sh`.

## Структура проекта

```text
django-resume/
├── resume_portfolio/               # Основные настройки проекта
├── pages/                          # Управление статическими страницами
├── projects/                       # Проекты (портфолио)
├── skills/                         # Навыки
├── shortlinks/                     # Сервис коротких ссылок
├── templates/                      # Общие шаблоны
├── static/                         # Статические файлы
├── media/                          # Загруженные пользователем файлы
├── manage.py
├── pyproject.toml                  # Зависимости для uv
├── requirements.txt                # Зависимости для Docker
├── Dockerfile                      # Сборка образа Django
├── docker-compose.yml              # Для разработки
├── docker-compose.prod.yml         # Для продакшена
├── deploy.sh                       # Скрипт деплоя
└── README.md
```

## Переменные окружения

| Переменная | Описание |
|------------|----------|
| `SECRET_KEY` | Секретный ключ Django |
| `DEBUG` | Режим отладки (`True`/`False`) |
| `ALLOWED_HOSTS` | Список разрешённых хостов через запятую без пробелов |
| `DB_NAME` | Имя базы данных PostgreSQL |
| `DB_USER` | Пользователь PostgreSQL |
| `DB_PASSWORD` | Пароль пользователя PostgreSQL |
| `ROLLBAR_ACCESS_TOKEN` | Токен для Rollbar (опционально) |
| `ROLLBAR_ENVIRONMENT` | Окружение для Rollbar (опционально) |
| `CSRF_TRUSTED_ORIGINS` | Доверенные источники для CSRF (продакшен) |
| `CSRF_COOKIE_SECURE` | `True` для HTTPS |
| `SESSION_COOKIE_SECURE` | `True` для HTTPS |

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
