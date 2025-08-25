# 🚀 Быстрый запуск проекта

## ⚡ Минимальная настройка для работы

### 1. Установка зависимостей
```bash
# Python пакеты
pip install -r requirements.txt

# Системные зависимости (Ubuntu/Debian)
sudo apt install redis-server -y
```

### 1.1. Настройка переменных окружения
```bash
# Копируем шаблон
cp env_vars.example.py env_vars.py

# Редактируем файл (замените на свои данные)
nano env_vars.py
```

### 2. Запуск всех сервисов
```bash
# Терминал 1: Redis
sudo systemctl start redis-server

# Терминал 2: Celery Worker
celery -A project_Tg worker --loglevel=info

# Терминал 3: Celery Beat
celery -A project_Tg beat --loglevel=info

# Терминал 4: Django сервер
python manage.py runserver

# Терминал 5: Telegram бот
python manage.py bot
```

## 🔑 Доступ к проекту

- **Веб-интерфейс:** http://localhost:8000/
- **Админ-панель:** http://localhost:8000/admin/
  - Создайте суперпользователя: `python manage.py createsuperuser`
  - Установите пароль: `python manage.py shell -c "from django.contrib.auth.models import User; u = User.objects.get(username='admin'); u.set_password('ваш_пароль'); u.save()"`

## ⚠️ Важно!

- **Redis обязателен** для рассылок и уведомлений
- **Celery Worker обязателен** для обработки задач
- **Все сервисы должны быть запущены** одновременно

## 🆘 Если что-то не работает

1. Проверьте, что Redis запущен: `redis-cli ping`
2. Проверьте процессы: `ps aux | grep -E "(celery|redis)"`
3. Смотрите подробную инструкцию: `REDIS_CELERY_SETUP.md`
