from django.http import HttpResponse
from django.shortcuts import render

from .forms import MyForm
from .models import MyModel


# Create your views here.

def home(request):
    # print("in home function")
    # if request.method == "POST":
    #     name=request.POST['name']
    #     email=request.POST['email']
    #     phone=request.POST['phone']
    #     message=request.POST['message']
    #     mymodel=MyModel(name=name,email=email,phone=phone,message=message)
    #     mymodel.save()
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about-us.html')


def contact(request):
    return render(request, 'contact-us.html')




def analyze(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        mymodel = MyModel(name=name, email=email,phone=phone ,message=message)
        mymodel.save()
    return render(request, 'home.html', {})
