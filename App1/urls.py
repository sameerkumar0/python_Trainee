from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("greet/",views.greet),
    path("<id>/",views.post)
]
