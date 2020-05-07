import os
from celery import Celery
from celery.schedules import crontab
from celery.decorators import task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agedcare.settings')
app = Celery('agedcare', broker='redis://h:pb66ea8c87345702a4d242151c3ddb19a9a0234bc6502490c8f6df9662f15d111@ec2-3-232-195-55.compute-1.amazonaws.com:24179')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
# inspect worker for the tasks 

i = app.control.inspect()
i.registered()
i.active()
i.scheduled


app.conf.beat_schedule = {
    'debug_task': {
        'task': 'agedcare.celery.debug_task',
        'schedule': crontab(minute="*"),
    },
    'weekly_report': {
        'task': 'health.tasks.weekly_pressure_report',
        'schedule': crontab(hour=7, minute=30, day_of_week="sunday"),
    },
    'monthly_pressure_report':{
        'task': 'health.tasks.monthly_pressure_report',
        'schedule': crontab(0, 0, day_of_month='1'),
    },
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))