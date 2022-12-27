from django.shortcuts import render
from home.models import Data
from home.forms import FormData
# Create your views here.
def home(request):
    data = Data.objects.all()
    
    context = {
        'data' : data,
    }
    return render(request, 'index.html',context)


def tambah(request):
    form = FormData()
    
    context = {
        'form' : form,
    }
    return render(request, 'tambah.html',context)