from django.shortcuts import redirect
from django.shortcuts import render 
from django.http import HttpResponse #Çıktıları görmek için
from .forms import ListForm
from .models import Formsayfasi
# Create your views here.

def index(request):        
    return render(request, "todoapp1/index.html", {})
    #index.html i gösterdik

def about(request):
    return render(request, "todoapp1/about.html", {})

def blog(request):
    return render(request, "todoapp1/blog.html", {})

def iletisim(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            form=ListForm()

    else:
        form=ListForm()

    context={
        "form":form
    }
    return render(request, "todoapp1/iletisim.html", context)


def sss(request):
    return render(request, "todoapp1/sss.html", {})

def proje(request):
    return render(request, "todoapp1/proje.html", {})
