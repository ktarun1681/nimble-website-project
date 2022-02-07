from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import contact
# Create your views here.

def index(request):
    # context = {"variable": "Tarun"}
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        Contact = contact(name =name, email= email, phone= phone, desc= desc, date = datetime.today())
        contact.save()

    return render(request, 'contact.html')



