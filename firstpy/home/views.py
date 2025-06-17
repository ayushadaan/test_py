from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message)
        contact.save()
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')


def ice_cream(request):
    return render(request, 'ice-cream.html')


def softy(request):
    return render(request, 'softy.html')


def family_pack(request):
    return render(request, 'family-pack.html')
