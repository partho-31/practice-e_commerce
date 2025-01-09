from django.urls import path
from .views import *

urlpatterns = [
    path('menu/',menu),
    path('next/<int : id>',next),
]