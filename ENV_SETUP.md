# 🔧 Настройка переменных окружения

## 📋 Что нужно настроить

Для работы проекта требуются следующие переменные:

1. **SECRET_KEY** - секретный ключ Django
2. **TELEGRAM_BOT_TOKEN** - токен вашего Telegram бота
3. **DEBUG** - режим отладки
4. **Настройки базы данных**
5. **Настройки Redis**

## 🚀 Быстрая настройка

### 1. Копирование шаблона
```bash
# Копируем файл-шаблон
cp env_vars.example.py env_vars.py
```

### 2. Редактирование файла
```bash
# Открываем файл в редакторе
nano env_vars.py
# или
code env_vars.py  # VS Code
# или
vim env_vars.py   # Vim
```

## 🔑 Заполнение переменных

### Django Settings
```python
# Секретный ключ Django (сгенерируйте новый!)
SECRET_KEY = 'django-insecure-ваш-новый-ключ-здесь'

# Режим отладки (True для разработки, False для продакшена)
DEBUG = True
```

### Telegram Bot Settings
```python
# Получите токен у @BotFather в Telegram
TELEGRAM_BOT_TOKEN = '123456789:ABCdefGHIjklMNOpqrsTUVwxyz'

# Ссылка для редиректа с главной страницы сайта на бота (если нужно)
# Когда пользователь заходит на ваш сайт, он автоматически перенаправляется на бота
# Замените на ссылку на вашего бота: https://t.me/your_bot_username
PROXY_URL = 'https://t.me/your_bot_username'
```

### Database Settings
```python
# SQLite (для разработки)
DATABASE_ENGINE = 'django.db.backends.sqlite3'
DATABASE_NAME = 'db.sqlite3'

# PostgreSQL (для продакшена)
# DATABASE_ENGINE = 'django.db.backends.postgresql_psycopg2'
# DATABASE_NAME = 'your_db_name'
# DATABASE_USER = 'your_db_user'
# DATABASE_PASSWORD = 'your_db_password'
# DATABASE_HOST = 'localhost'
# DATABASE_PORT = '5432'
```

### Redis Settings
```python
# Локальный Redis
REDIS_URL = 'redis://localhost:6379/0'

# Redis с паролем
# REDIS_URL = 'redis://:password@localhost:6379/0'

# Redis на удаленном сервере
# REDIS_URL = 'redis://user:password@redis.example.com:6379/0'
```

## 🔐 Генерация SECRET_KEY

### Автоматическая генерация
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Ручная замена
Замените строку в `env_vars.py`:
```python
SECRET_KEY = 'сгенерированный-ключ-здесь'
```

## 📱 Получение токена бота

### 1. Напишите @BotFather в Telegram
### 2. Отправьте команду `/start`
### 3. Отправьте команду `/newbot`
### 4. Введите имя бота
### 5. Введите username (должен заканчиваться на 'bot')
### 6. Скопируйте полученный токен

## 🔗 Настройка PROXY_URL

### Что это такое?
`PROXY_URL` - это ссылка, на которую пользователи будут перенаправляться, когда заходят на главную страницу вашего сайта.

### Как это работает?
1. Пользователь заходит на `http://localhost:8000/`
2. Django автоматически перенаправляет его на `PROXY_URL`
3. Пользователь попадает на вашего бота в Telegram

### Примеры настроек:
```python
# На вашего бота
PROXY_URL = 'https://t.me/my_anonymous_chatbot'

# На группу бота
PROXY_URL = 'https://t.me/my_bot_group'

# На внешний сайт
PROXY_URL = 'https://mywebsite.com'

# Отключить редирект (оставить пустым)
PROXY_URL = ''
```

## ✅ Проверка настроек

### 1. Проверка Django
```bash
python manage.py check
```

### 2. Проверка подключения к Redis
```bash
redis-cli ping  # Должен ответить "PONG"
```

### 3. Проверка токена бота
```bash
python manage.py shell -c "from django.conf import settings; print('TOKEN:', settings.TOKEN)"
```

## 🚨 Важные замечания

### Безопасность
- **Никогда не коммитьте** `env_vars.py` в git
- **Не делитесь** токенами с посторонними
- **Используйте разные токены** для разработки и продакшена

### Файлы
- `env_vars.example.py` - **шаблон** (можно коммитить)
- `env_vars.py` - **реальные данные** (НЕ коммитить!)

### Продакшен
- Измените `DEBUG = False`
- Используйте сложные пароли
- Ограничьте доступ к Redis
- Используйте HTTPS

## 🆘 Решение проблем

### Ошибка "ModuleNotFoundError: No module named 'env_vars'"
```bash
# Файл не найден
ls -la env_vars.py

# Если файла нет, скопируйте шаблон
cp env_vars.example.py env_vars.py
```

### Ошибка "TOKEN not found"
```bash
# Проверьте, что TOKEN указан в env_vars.py
grep "TELEGRAM_BOT_TOKEN" env_vars.py

# Проверьте, что файл импортируется
python manage.py check
```

### Ошибка подключения к Redis
```bash
# Проверьте, что Redis запущен
sudo systemctl status redis-server

# Проверьте подключение
redis-cli ping
```
