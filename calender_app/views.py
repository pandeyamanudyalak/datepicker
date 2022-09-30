from django.shortcuts import render
from .form import CalenderForm
from django.http import HttpResponse
from .models import Calender

# Create your views here.

def Home(request):
    if request.method=='POST':
        print('------------------------------')
        date = request.POST.get('datefield')
        print('------------------------------',date)
        data = Calender(datefield=date)
        data.save()
    
    
    form = CalenderForm()
    
    return render(request,'index.html',{'form':form})