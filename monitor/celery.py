import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE','monitor.settings')

app = Celery('monitor')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()

app.conf.beat_schedule = {
	'get_temperature':{
		'task': 'temperatura.tasks.get_temperature',
		'schedule': crontab(minute=0, hour='*/1')
	},
	'delete_temperature':{
		'task': 'temperatura.tasks.delete_temperature',
		'schedule': crontab()
	}
}

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

