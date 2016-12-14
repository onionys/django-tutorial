from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.

from django.shortcuts import render
from datetime import datetime

def hello_world(request):
    print(type(request))
    print(dir(request))
    # return HttpResponse("hello")
    data = dict()
    data['current_time'] = str(datetime.now())
    return render(request, "hello_world.html", data)



def home(request):
    post_list = Post.objects.all()
    data = dict()
    data['post_list'] = post_list
    return render(request, "home.html", data)
