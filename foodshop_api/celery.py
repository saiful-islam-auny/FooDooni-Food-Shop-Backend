from __future__ import absolute_import, unicode_literals
import os
from celery import Celery  # ✅ CORRECT IMPORT

# Set default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodshop_api.settings')

# Create Celery app
app = Celery('foodshop_api')

# Load settings from Django settings, using namespace CELERY
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks from all registered apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
