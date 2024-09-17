from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    dis = {
        'name' : ['samin', 'rohim', 'korim'],
        'Current_date' : datetime.datetime.now(),
        'animals': 'cat\ndog\nhorse',
        'text' : 'I Am Master Yoda'
         
    }
    return render(request, 'home.html', dis)