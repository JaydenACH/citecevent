from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('recordemail', views.recordemail, name="recordemail"),
]
