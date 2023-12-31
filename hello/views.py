from django.shortcuts import render

#from .models import Greeting




def index(request):
    return render(request,'Myapp/index.html')

# Create your views here.