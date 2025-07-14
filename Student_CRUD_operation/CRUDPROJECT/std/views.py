from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Q 
from .models import *
# Create your views here.
def home(request):
    data=Student.objects.all()
    return render(request,"std/home.html",{"data":data})

def std_add(request):
    if request.method=='POST':
        std_roll=request.POST.get('rollno')
        std_name=request.POST.get('username')
        std_email=request.POST.get('emailid')
        std_address=request.POST.get('addressid')
        std_phone=request.POST.get('phoneno')

        #create an object for models
        if Student.objects.filter(Q(roll=std_roll) | Q(email=std_email)).exists():
            messages.error(request, "A student with this roll number or emailid already exists.")
            s=Student()
        else:
            s=Student()
            s.roll=std_roll
            s.name=std_name
            s.email=std_email
            s.address=std_address
            s.phone=std_phone
            s.save()
            return redirect("home")
    
    return render(request, 'std/std_add.html')

#this function will Delete
def delete_data(request,id):
    if request.method=="POST":
        data=Student.objects.get(pk=id)
        data.delete()
    return redirect("home")
    
#This Function Will Update/Edit
def update_data(request,id):
    if request.method=='POST':
        std=Student.objects.get(pk=id)
        std_roll=request.POST.get('rollno')
        std_name=request.POST.get('username')
        std_email=request.POST.get('emailid')
        std_address=request.POST.get('addressid')
        std_phone=request.POST.get('phoneno')

        std.roll=std_roll
        std.name=std_name
        std.email=std_email
        std.address=std_address
        std.phone=std_phone
        std.save()
        return redirect("home")
        
    else:
        data=Student.objects.get(pk=id)

    return render(request, 'std/studentupdate.html',{'std':data})