from . import views
from django.urls import path

app_name = 'timetable'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:group_id>', views.generate, name='generate'),
]