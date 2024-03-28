from celery import shared_task

@shared_task(bind=True)
def my_celery_task(self):
    for i in range(500):
        for j in range(i):
            print(i*j)