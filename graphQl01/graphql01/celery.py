import os

from celery import Celery
from decouple import config
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE","graphql01.settings")

celery_app = Celery("graphql01")

celery_app.conf.update(
    {
        "broker_url": config("CELERY_BROKER_URL"),
        "task_serializer": "json",
        "task_acks_late": True,
        "result_serializer": "json",
        # "result_backend": "django-db",
        "accept_content": ["json"],
        "worker_prefetch_multiplier": 1,
        "result_extended": True,
        "task_reject_on_worker_lost": True,
    }
)
celery_app.conf.task_routes = {"main.tasks.my_celery_task":{"queue":"test_queue"}}
celery_app.config_from_object(settings, namespace="graphql_celery")
celery_app.autodiscover_tasks()
