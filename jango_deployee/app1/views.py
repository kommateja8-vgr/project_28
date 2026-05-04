from django.shortcuts import render,redirect


# Create your views here.

from app1.models import Employee

from app1.forms import Employee_form

def new_employee(request):

    data = Employee.objects.all()

    form = Employee_form()

    if request.method == 'POST':
        form = Employee_form(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home_page')
        
    context = {
        'data':data,
        'form':form
    }
    return render(request,'home.html',context)



