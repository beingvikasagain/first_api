import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery01.settings")

celery_app = Celery("celery01")

celery_app.conf.update(
    {
        "broker_url": "amqp://root:root@rabbitmqserver",
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

celery_app.conf.task_routes = {
    "main.tasks.long_run_count":{"queue":"testq"}
}
celery_app.config_from_object(settings, namespace="test_celery01")
celery_app.autodiscover_tasks()
