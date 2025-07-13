from django.shortcuts import render,redirect,get_object_or_404
from .forms import Employeeform
from .models import *
from django.db.models import Q
# Create your views here.
def employee_list(request):
    data=Employee.objects.all()
    return render(request,"employee_register/employee_list.html", {"data":data})

def employee_form(request,id=0):
    if request.method=="GET":
        if id == 0:
            form=Employeeform()
        else:
            instance = get_object_or_404(Employee, pk=id)
            form = Employeeform(instance=instance)
        return render(request,"employee_register/employee_form.html",{"fm":form})
    
    else:
        if id == 0: 
            form=Employeeform(request.POST)
        else:
            instance = get_object_or_404(Employee, pk=id)
            form = Employeeform(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        else:
            return render(request, "employee_register/employee_form.html", {"fm": form, "id": id})
        return redirect('listData')

def employee_delete(request,id):
    if request.method=='POST':
        data=Employee.objects.get(pk=id)
        data.delete()
    return redirect('listData')


