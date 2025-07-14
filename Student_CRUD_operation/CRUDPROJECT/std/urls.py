from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path("add/",std_add,name="std_add"),
    path('delete/<id>/',delete_data,name="deleteData"),
    path('update/<id>/',update_data, name='updateData'),
]