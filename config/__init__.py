from __future__ import absolute_import, unicode_literals
# импортируем приложение Celery
from .celery import app as celery_app

# Экспортируем Celery как часть модуля
__all__ = ('celery_app',)
