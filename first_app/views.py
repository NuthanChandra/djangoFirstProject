from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    my_dict = {'thingVar': 'Hallo amigos, I am thingVar from first_app/views.py'}
    return render(request,'first_app/index.html',context=my_dict)