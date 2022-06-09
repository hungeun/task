from django.urls import path
from . import views

urlpatterns =[
    path('',views.map_, name='map_'),
    path('',views.task, name='task'),
]