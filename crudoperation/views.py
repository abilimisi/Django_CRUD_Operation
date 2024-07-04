from django.shortcuts import render, HttpResponseRedirect
from .forms import Studentregistration
from .models import User
from django.contrib import messages


# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = Studentregistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            reg = User(name=name, email=email, password=password)
            reg.save()
            messages.success(request, 'Information added successfully')
            fm = Studentregistration()
    else:
        fm = Studentregistration()
    stud = User.objects.all()
    return render(request, 'enroll/index.html', {'form': fm, 'stu': stud})


def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        messages.success(request, 'Information deleted successfully')
        return HttpResponseRedirect('/')


def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = Studentregistration(request.POST, instance=pi)
        if fm.is_valid:
            fm.save()
            return HttpResponseRedirect('/')
            messages.success(request, 'Information updated successfully')
    else:
        pi = User.objects.get(pk=id)
        fm = Studentregistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form': fm})
