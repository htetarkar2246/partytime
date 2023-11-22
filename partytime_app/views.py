from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog,Contact,Service

# Create your views here.
def partytime(request):
    return render(request, 'index.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html',{'services':services})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        contact = Contact()
        contact.name=request.POST['name'],
        contact.email=request.POST['email'],
        contact.phone=request.POST['phone'],
        contact.message=request.POST['message']
        contact.save()
        return redirect('contact') 
    else:
        return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs.html' ,{'blogs':blogs})

def checkout(request):
    return render(request, 'checkout.html')

def blog_display(request,description):
    blog = Blog.objects.get(id = description)
    return render(request, 'blog.html' , {'blog':blog})
