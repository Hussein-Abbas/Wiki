from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/", views.index),
    path("wiki/search", views.search, name="search"),
    path("wiki/newpage", views.newpage, name="newpage"),
    path("wiki/randompage", views.randompage, name="randompage"),
    path("wiki/<str:title>/editpage", views.editpage, name="editpage"),
    path("wiki/<str:title>", views.entry, name="entry"),
]
