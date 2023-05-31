from django.urls import path
from . import views


#tells us what functions to run when the user/client hits a specified URL

urlpatterns = [
    path("", views.index),
    path("<int:season>", views.seasonPage)
]