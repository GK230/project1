from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/search", views.search, name="search_results"),
    path("wiki/<title>", views.entry, name="entry"),
    path("wiki/error", views.entry, name="error"),


]
