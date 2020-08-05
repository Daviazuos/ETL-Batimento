from celery import Celery

broker_url = f"amqp://{'rabbit'}:{'rabbit'}@{'localhost'}//"

app = Celery('batimento_Broker', broker=broker_url, include=['dags.Common'])

app.autodiscover_tasks([
    'dags.Common.OpenFile.OpenFile'
], force=True)