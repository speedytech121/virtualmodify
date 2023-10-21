
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


# def analyze(request):
#     namedata = request.POST.get('name', default="")
#     emaildata = request.POST.get('email', default="")
#     messagedata = request.POST.get('message', default="")
#     params = {'name': namedata, 'email': emaildata, 'message': messagedata}
#     print(params)
#     return render(request, 'analyze.html', params)
