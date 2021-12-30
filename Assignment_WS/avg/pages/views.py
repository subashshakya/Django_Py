from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home(request):
    return render(request, 'pages/home.html')


def recieve(request):
    if request.method == 'GET':
        num1 = int(request.GET.get('num1'))
        num2 = int(request.GET.get('num2'))
        avg = (num1 + num2) / 2
        return HttpResponse(f"The average of the two numbers {num1=} and {num2=} is: {avg=}")


def about(request):
    return HttpResponse('this is working')


