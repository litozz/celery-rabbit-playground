from celery import Celery

app = Celery('celery_sample', backend='rpc://', broker='rabbitmq')


if __name__ == '__main__':
    app.start()
