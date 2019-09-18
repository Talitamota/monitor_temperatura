import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE','monitor.settings')

app = Celery('monitor')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()

app.conf.beat_schedule = {
	'printa_mensagem_no_termial':{
		'task': 'temperatura.tasks.testando_a_task',
		'schedule':crontab()
	},
}

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

