from email import message
from multiprocessing import context
from pyexpat.errors import messages
from django.shortcuts import render,redirect

from todoapp.models import TodoModel
from .forms import *
# Create your views here.


def home(request):
    sq=TodoModel.objects.all()
    context={
        'sq':sq
    }
    return render(request,'home.html',context)

def add(request):
    if request.method == 'POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home') 
    else:
        form=TodoForm()
        return render(request,'add.html',{'form':form}) 

def updatetask(request,id):
    sq=TodoModel.objects.get(id=id)

    form=TodoForm(instance=sq)
    if request.method=='POST':
        form=TodoForm(request.POST,instance=sq)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('home')
    return render(request,'update.html',{'form':form})


def deleteTask(request,id):
    form=TodoForm()
    if request.method=='POST':
        TodoModel.objects.get(id=id).delete()
        return redirect('home')
    # else:
    #     return redirect('home')
    return render(request,'delete.html')




# def create(request,*args, **kwargs):
#     id=kwargs.get("id")

#     sq=TodoModel.objects.get(id=id)

#     form=forms.TodoForm(instance=sq)
#     if request.method == 'POST':
#         form=forms.TodoForm(request.POST)
#         if form.is_valid():
#             TodoModel.objects.filter(id=id).update(form)

#         return redirect('home')
#     return render(request,'details.html',{'form':form})