from django.urls import path
from .views import *
urlpatterns = [
     path("",employee_form,name="employeeForm"),
    path("<int:id>/",employee_form,name="employeeUpdate"),
    path("list/",employee_list,name='listData'),
    path("delete/<int:id>/",employee_delete,name="employeeDelete"),
]