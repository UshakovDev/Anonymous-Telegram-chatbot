# -*- coding: utf-8 -*-
"""
ФАЙЛ-ШАБЛОН для переменных окружения
Скопируйте этот файл в env_vars.py и заполните актуальными данными

ВАЖНО: Никогда не коммитьте env_vars.py в git!
"""

import os
from pathlib import Path

# Django Settings
SECRET_KEY = 'django-insecure-your-secret-key-here-change-this-in-production'
DEBUG = True

# Database Settings
DATABASE_ENGINE = 'django.db.backends.sqlite3'
DATABASE_NAME = 'db.sqlite3'

# Telegram Bot Settings
TELEGRAM_BOT_TOKEN = 'your-telegram-bot-token-here'

# Ссылка для редиректа с главной страницы сайта на бота
# Замените на ссылку на вашего бота: https://t.me/your_bot_username
PROXY_URL = 'https://t.me/your_bot_username'

# Redis Settings
REDIS_URL = 'redis://localhost:6379/0'

# Media and Static Files
MEDIA_ROOT = 'media/'
STATIC_ROOT = 'static/'
