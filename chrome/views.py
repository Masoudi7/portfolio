from django.shortcuts import render
#from django.http import HttpResponse
from .models import Article
# Create your views here.


def home(request):
    context={
        'ENG':Article.objects.filter(status='p').order_by('-publish')[:3]
    }
    return render(request,'chrome/home.html',context)




def detail(request,slug):
    context={
        'ENG':Article.objects.get(slug=slug)
    }
    return render(request,'chrome/detail.html',context)