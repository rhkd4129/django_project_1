from django.shortcuts import render
from .melonchart import my_dict
# Create your views here.

def melon_chart(request):
    return render(request,'crawling/melon_chart.html',{'melon_chart':my_dict,})