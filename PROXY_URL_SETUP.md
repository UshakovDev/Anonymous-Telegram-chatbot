# 🔗 Настройка PROXY_URL

## 📋 Что такое PROXY_URL?

`PROXY_URL` - это ссылка для **автоматического перенаправления** пользователей с главной страницы вашего сайта на Telegram бота.

## 🚀 Как это работает?

1. **Пользователь заходит на сайт** → `http://localhost:8000/`
2. **Django автоматически перенаправляет** на `PROXY_URL`
3. **Пользователь попадает на бота** → начинает общение

## ⚙️ Настройка

### 1. Получите username вашего бота
- Напишите боту @BotFather
- Используйте команду `/mybots`
- Скопируйте username (без символа `@`)

### 2. Установите PROXY_URL
```python
# В файле env_vars.py
PROXY_URL = 'https://t.me/your_bot_username'
```

### 3. Примеры
```python
# Если username бота: @anonymous_chat_bot
PROXY_URL = 'https://t.me/anonymous_chat_bot'

# Если username бота: @dating_bot
PROXY_URL = 'https://t.me/dating_bot'

# Если username бота: @my_bot_123
PROXY_URL = 'https://t.me/my_bot_123'
```

## 🔧 Варианты использования

### Перенаправление на бота
```python
PROXY_URL = 'https://t.me/your_bot_username'
```

### Перенаправление на группу
```python
PROXY_URL = 'https://t.me/your_bot_group'
```

### Перенаправление на внешний сайт
```python
PROXY_URL = 'https://yourwebsite.com'
```

### Отключить редирект
```python
PROXY_URL = ''  # Пустая строка
```

## ✅ Проверка

1. **Сохраните файл** `env_vars.py`
2. **Перезапустите Django сервер**
3. **Откройте** `http://localhost:8000/`
4. **Должен произойти редирект** на вашего бота

## 🚨 Важно!

- **Username бота** должен существовать
- **Ссылка должна быть корректной** (https://t.me/username)
- **После изменения** перезапустите сервер
- **Проверьте редирект** в браузере

## 🆘 Если не работает

1. **Проверьте username бота** - он должен существовать
2. **Проверьте формат ссылки** - `https://t.me/username`
3. **Перезапустите Django сервер**
4. **Очистите кэш браузера**
