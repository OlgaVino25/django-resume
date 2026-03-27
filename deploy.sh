set -e

echo "Обновляем код из репозитория..."
git pull origin main

echo "Проверяем наличие .env файла..."
if [ ! -f .env ]; then
    echo "Ошибка: файл .env не найден. Скопируйте .env.example и заполните его."
    exit 1
fi

echo "Останавливаем старые контейнеры..."
docker-compose -f docker-compose.prod.yml down

echo "Собираем и запускаем новые контейнеры..."
docker-compose -f docker-compose.prod.yml up -d --build

echo "Применяем миграции..."
docker-compose -f docker-compose.prod.yml exec -T web python manage.py migrate

echo "Собираем статику (в образе уже собрана, но на всякий случай)..."
docker-compose -f docker-compose.prod.yml exec -T web python manage.py collectstatic --noinput

echo "Копируем статику на хост для Nginx..."
mkdir -p /opt/resume/staticfiles
docker cp $(docker-compose -f docker-compose.prod.yml ps -q web):/app/staticfiles/. /opt/resume/staticfiles/

echo "Копируем медиа на хост для Nginx..."
mkdir -p /opt/resume/media
docker cp $(docker-compose -f docker-compose.prod.yml ps -q web):/app/media/. /opt/resume/media/
chmod -R 755 /opt/resume/media

echo "Деплой завершён успешно!"