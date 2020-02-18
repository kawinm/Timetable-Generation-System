
from . import views
from django.urls import path

app_name = 'datamgmt'
urlpatterns = [
    path('', views.index, name='index'),
]