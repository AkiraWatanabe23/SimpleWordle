'''urlの記述'''
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("result", views.view_result, name="result"),
    path("play", views.play, name="play")
]
