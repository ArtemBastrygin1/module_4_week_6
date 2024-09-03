from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Устанавливаем переменную окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('task_manager')

# Загружаем конфигурацию из настроек Django, используя пространство имен CELERY
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находим и регистрируем задачи из всех приложений Django
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
