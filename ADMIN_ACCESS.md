# 🔐 Доступ к админ-панели

## 📱 Создание суперпользователя

### 1. Создание пользователя
```bash
python manage.py createsuperuser
# Введите username, email и пароль
```

### 2. Установка пароля (если создали без пароля)
```bash
python manage.py shell -c "from django.contrib.auth.models import User; u = User.objects.get(username='admin'); u.set_password('ваш_пароль'); u.save()"
```

### 3. Альтернативный способ создания
```bash
# Создание с паролем через shell
python manage.py shell
```
```python
from django.contrib.auth.models import User
User.objects.create_superuser('admin', 'admin@example.com', 'ваш_пароль')
```

## 🌐 Ссылки

- **Админ-панель:** http://localhost:8000/admin/
- **Веб-интерфейс:** http://localhost:8000/

## ⚠️ Важно

- **Создавайте уникальных суперпользователей** для каждого проекта
- **Используйте сложные пароли** (минимум 8 символов, буквы + цифры + символы)
- **Регулярно обновляйте пароли** для безопасности
- **Не используйте пароли по умолчанию** в продакшене

## 🔧 Изменение пароля

Для изменения пароля используйте Django shell:

```bash
python manage.py shell
```

```python
from django.contrib.auth.models import User
u = User.objects.get(username='admin')  # замените на ваш username
u.set_password('новый_пароль')
u.save()
```

### Быстрый способ через командную строку:
```bash
python manage.py shell -c "from django.contrib.auth.models import User; u = User.objects.get(username='admin'); u.set_password('новый_пароль'); u.save()"
```
