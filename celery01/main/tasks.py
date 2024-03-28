from time import perf_counter

from celery import shared_task


@shared_task(bind=True)
def long_run_count(self):
    start_time = perf_counter()
    for i in range(100000):
        for j in range(i):
            a = i*j
            print(a)
    end_time = perf_counter()
    return round((end_time-start_time),2)