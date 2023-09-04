from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import *
from django.shortcuts import redirect
def show_about_page(request):
    print("about page request")
    name='rishabh'
    link='https://www.youtube.com/rishabh9913'
    
    data={
        'name': name,
        'link': link
    }
    
    return render(request,"about.html",data)


def show_home_page(request):
    cats=Category.objects.all()
    Images=Image.objects.all()
    
    data = {'images':Images,'cats':cats }
    
    
    return render(request,"home.html",data)


def show_category_page(request,cid):
    print(cid)
    cats=Category.objects.all()
    
    category= Category.objects.get(pk=cid)
    
    Images=Image.objects.filter(Category=category)
    
    data = {'images':Images,'cats':cats }
    
    
    return render(request,"home.html",data)


def home(request):
    return redirect('/home')
####
def search(request):
    return HttpResponse('This is search bar,but it is empty')
