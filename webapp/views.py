from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.
def emp_register(request):
    form = emp_form()
    if request.method == "POST":
        form = emp_form(request.POST)
        if form.is_valid:
            form.save()
            return redirect('emp_list')
    context = {'form':form}
    return render(request,'emp_register.html',context)

def emp_list(request):
    employeelist = Employee.objects.all()
    context = {'listofemployees':employeelist}
    return render(request,'emp_list.html',context )

def update_emp_list(request, pk):
    employeelist = Employee.objects.get(id=pk)
    updateform = emp_form(instance=employeelist)
    if request.method == "POST":
        form = emp_form(request.POST, instance=employeelist)
        if form.is_valid:
            form.save()
            return redirect('emp_list')
    context ={'form':updateform}
    return render(request,'emp_register.html',context)

def del_emp(request, pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return redirect('emp_list')