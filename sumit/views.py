from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.from django.shortcuts import render
from django.contrib import messages
from .models import message

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def skills(request):
    return render(request, 'skills.html')

def projects(request):
    return render(request, 'projects.html')

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('Entername')
        email = request.POST.get('Enteremail')
        phoneno = request.POST.get('Enterphoneno')
        message_content = request.POST.get('Entermessage')
        new_message = message(
            name=name, 
            email=email, 
            phoneno=phoneno, 
            message=message_content
        )
        new_message.save()
        messages.success(request, "Your message has been delivered.")
        return redirect('/contact/')
    return render(request, 'contact.html')
