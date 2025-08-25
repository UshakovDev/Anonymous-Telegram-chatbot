# 🔧 Настройка Redis и Celery

## 📋 Обязательные компоненты

Для полноценной работы бота (рассылки, уведомления) требуются:

1. **Redis** - сервер кэширования и очередей
2. **Celery Worker** - обработчик асинхронных задач
3. **Celery Beat** - планировщик задач

## 🚀 Установка Redis

### Ubuntu/Debian
```bash
sudo apt update
sudo apt install redis-server -y
```

### CentOS/RHEL
```bash
sudo yum install redis -y
```

### macOS
```bash
brew install redis
```

## ⚙️ Настройка Redis

### 1. Запуск сервиса
```bash
# Запуск
sudo systemctl start redis-server

# Автозапуск при загрузке системы
sudo systemctl enable redis-server

# Проверка статуса
sudo systemctl status redis-server
```

### 2. Проверка работы
```bash
# Проверка подключения
redis-cli ping  # Должен ответить "PONG"

# Проверка порта
netstat -tlnp | grep :6379
```

### 3. Настройка безопасности (опционально)
```bash
# Редактирование конфигурации
sudo nano /etc/redis/redis.conf

# Основные настройки:
# bind 127.0.0.1  # Только локальные подключения
# requirepass ваш_пароль  # Пароль (не забудьте обновить в settings.py)
```

## 🔄 Настройка Celery

### 1. Проверка зависимостей
```bash
# Убедитесь, что установлены
pip install celery redis
```

### 2. Запуск Celery Worker
```bash
# В отдельном терминале
celery -A project_Tg worker --loglevel=info

# Или в фоновом режиме
celery -A project_Tg worker --loglevel=info &
```

### 3. Запуск Celery Beat
```bash
# В отдельном терминале
celery -A project_Tg beat --loglevel=info

# Или в фоновом режиме
celery -A project_Tg beat --loglevel=info &
```

## 📱 Проверка работы

### 1. Проверка процессов
```bash
# Проверка Redis
ps aux | grep redis-server | grep -v grep

# Проверка Celery
ps aux | grep celery | grep -v grep
```

### 2. Проверка очередей
```bash
# Подключение к Redis
redis-cli

# Просмотр очередей
KEYS *
```

### 3. Тест рассылки
1. Откройте админ-панель: http://localhost:8000/admin/
2. Попробуйте сделать рассылку пользователям
3. Проверьте логи Celery worker

## 🚨 Решение проблем

### Redis не запускается
```bash
# Проверка логов
sudo journalctl -u redis-server

# Перезапуск
sudo systemctl restart redis-server
```

### Celery не подключается к Redis
```bash
# Проверка настроек в settings.py
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# Проверка подключения Redis
redis-cli ping
```

### Рассылка не работает
1. Убедитесь, что Redis запущен
2. Убедитесь, что Celery worker запущен
3. Проверьте логи Django и Celery
4. Проверьте токен бота

## 📊 Мониторинг

### Логи Celery
```bash
# Worker логи
tail -f celery.log

# Beat логи
tail -f celerybeat.log
```

### Статус Redis
```bash
# Информация о Redis
redis-cli info

# Мониторинг в реальном времени
redis-cli monitor
```

## 🔒 Безопасность

### Продакшен настройки
```bash
# Ограничение доступа только с localhost
sudo nano /etc/redis/redis.conf
# bind 127.0.0.1

# Установка пароля
sudo nano /etc/redis/redis.conf
# requirepass сложный_пароль

# Обновление settings.py
CELERY_BROKER_URL = 'redis://:пароль@localhost:6379/0'
```

### Firewall
```bash
# Блокировка внешнего доступа к Redis
sudo ufw deny 6379
```

## 📝 Полезные команды

```bash
# Остановка всех процессов
sudo systemctl stop redis-server
pkill -f "celery.*worker"
pkill -f "celery.*beat"

# Перезапуск всех сервисов
sudo systemctl restart redis-server
celery -A project_Tg worker --loglevel=info &
celery -A project_Tg beat --loglevel=info &
```
