# Anonymous Telegram Chatbot

Анонимный Telegram бот для поиска собеседников с функциями поиска по полу, автоматической блокировки по рейтингу, уведомлений и рекламы.

## 🚀 Быстрый старт

### 1. Клонирование репозитория
```bash
git clone https://github.com/UshakovDev/Anonymous-Telegram-chatbot.git
cd Anonymous-Telegram-chatbot
```

### 2. Создание виртуального окружения
```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# или
.venv\Scripts\activate  # Windows
```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
pip install django psycopg2-binary
```

### 3.1. Установка системных зависимостей
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install redis-server -y

# CentOS/RHEL
sudo yum install redis -y

# macOS
brew install redis
```

### 4. Настройка переменных окружения
Скопируйте файл-шаблон и заполните актуальными данными:

```bash
# Копируем шаблон
cp env_vars.example.py env_vars.py

# Редактируем файл
nano env_vars.py  # или любой текстовый редактор
```

```python
# Django Settings
SECRET_KEY = 'ваш-секретный-ключ-django'
DEBUG = True

# Telegram Bot Settings
TELEGRAM_BOT_TOKEN = 'ваш-токен-бота-от-botfather'

# Ссылка для редиректа с главной страницы сайта на бота
# Замените на ссылку на вашего бота: https://t.me/your_bot_username
PROXY_URL = 'https://t.me/your_bot_username'

# Database Settings
DATABASE_ENGINE = 'django.db.backends.sqlite3'  # или postgresql
DATABASE_NAME = 'db.sqlite3'

# Redis Settings
REDIS_URL = 'redis://localhost:6379/0'
```

### 5. Настройка базы данных
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

**Важно:** После создания суперпользователя установите пароль:
```bash
python manage.py shell -c "from django.contrib.auth.models import User; u = User.objects.get(username='admin'); u.set_password('ваш_пароль'); u.save()"
```

### 6. Запуск проекта
```bash
# 1. Запуск Redis (обязательно!)
sudo systemctl start redis-server
sudo systemctl enable redis-server  # автозапуск при загрузке

# 2. Запуск Celery worker (в отдельном терминале)
celery -A project_Tg worker --loglevel=info &

# 3. Запуск Celery beat (в отдельном терминале)
celery -A project_Tg beat --loglevel=info &

# 4. Веб-интерфейс (в отдельном терминале)
python manage.py runserver

# 5. Telegram бот (в отдельном терминале)
python manage.py bot
```

## 🔧 Конфигурация

### Получение токена бота
1. Напишите @BotFather в Telegram
2. Создайте нового бота командой `/newbot`
3. Скопируйте полученный токен в `env_vars.py`

### Настройка PROXY_URL
`PROXY_URL` - это ссылка для автоматического перенаправления пользователей с главной страницы сайта на вашего бота в Telegram.

**Пример:** Если username вашего бота `@my_anonymous_chatbot`, то установите:
```python
PROXY_URL = 'https://t.me/my_anonymous_chatbot'
```

**Как это работает:** Пользователь заходит на ваш сайт → автоматически перенаправляется на бота → начинает общение.

### База данных
По умолчанию используется SQLite. Для продакшена рекомендуется PostgreSQL.

### Redis
Требуется для работы Celery (асинхронные задачи).

**Важно:** Redis должен быть запущен для работы рассылок и асинхронных задач!

```bash
# Проверка статуса Redis
sudo systemctl status redis-server

# Проверка подключения
redis-cli ping  # Должен ответить "PONG"
```

### Celery
Обрабатывает асинхронные задачи (рассылки, уведомления).

**Компоненты:**
- **Worker** - обрабатывает задачи
- **Beat** - планировщик задач
- **Redis** - брокер сообщений

## 📁 Структура проекта

- `project_Tg/` - основная конфигурация Django
- `Bot_app_Tg/` - логика Telegram бота
- `static/` - статические файлы
- `templates/` - HTML шаблоны
- `env_vars.py` - переменные окружения

## 🌐 Доступ

- **Веб-интерфейс:** http://localhost:8000/
- **Админ-панель:** http://localhost:8000/admin/
  - Создайте суперпользователя: `python manage.py createsuperuser`
  - Установите пароль: `python manage.py shell -c "from django.contrib.auth.models import User; u = User.objects.get(username='admin'); u.set_password('ваш_пароль'); u.save()"`

## ⚠️ Безопасность

- Никогда не коммитьте `env_vars.py` в git
- Измените SECRET_KEY в продакшене
- Используйте HTTPS в продакшене
- Ограничьте доступ к админ-панели

## 📚 Дополнительная документация

- **[QUICK_START.md](QUICK_START.md)** - Быстрый запуск проекта
- **[ENV_SETUP.md](ENV_SETUP.md)** - Настройка переменных окружения
- **[PROXY_URL_SETUP.md](PROXY_URL_SETUP.md)** - Настройка перенаправления на бота
- **[REDIS_CELERY_SETUP.md](REDIS_CELERY_SETUP.md)** - Подробная настройка Redis и Celery
- **[BOT_SETUP.md](BOT_SETUP.md)** - Настройка Telegram бота
- **[ADMIN_ACCESS.md](ADMIN_ACCESS.md)** - Доступ к админ-панели
- **[NEWSLETTER_GUIDE.md](NEWSLETTER_GUIDE.md)** - Руководство по рассылке через админ-панель

## 📝 Лицензия

MIT License

Полный текст лицензии доступен в файле [LICENSE](LICENSE).
