from django.urls import path
from . import views

urlpatterns = [
    path("!manage/<str:short_url>/", views.manage, name="manage"),
    path("!manage/", views.manage, name="manage"),
    path("<str:short_url>/", views.redirect, name="redirect"),
    path("", views.IndexView.as_view(), name="index"),
    # Add more URL patterns here
]
