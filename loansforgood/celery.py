from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loansforgood.settings')

app = Celery('loansforgood')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.update(
    result_expires=3600,
    enable_utc = True,
    timezone = 'America/Sao_Paulo'
)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
