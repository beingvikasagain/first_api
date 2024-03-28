from celery import Celery

from graphql01.celery import celery_app

__all__ = ("celery_app",)
