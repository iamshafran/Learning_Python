from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.viewEntry, name="entry"),
    path("search/", views.searchResults, name="search"),
    path("newPage/", views.newPage, name="new"),
    path("<str:title>/edit/", views.editEntry, name="edit"),
    path("random/", views.randomPage, name="random"),
]
