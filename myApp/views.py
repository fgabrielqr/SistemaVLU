from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def msg(request):
    return render(request, 'myApp/index.html')
