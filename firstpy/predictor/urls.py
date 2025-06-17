# predictor/urls.py
from django.urls import path
from .views import check_fitness

urlpatterns = [
    path('predict/', check_fitness),
]
