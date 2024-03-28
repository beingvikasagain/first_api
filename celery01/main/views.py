from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import generic

from .tasks import long_run_count


# class CeleryTest(generic.CreateView):
def celery_test(request):
    long_run_count.delay()
    return HttpResponse("tested")
