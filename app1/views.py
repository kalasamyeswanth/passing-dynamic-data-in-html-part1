from django.shortcuts import render
from .models import Destination
# Create your views here.
def link1(request):
    return render(request,'index.html')
def link2(request):
    dest1 = Destination()
    dest1.name = 'yeswanth'
    dest1.prize = 1888
    dest1.desc = 'this is the place with lot of flowers'
    return render(request,'index2.html',{'dd' : dest1})

