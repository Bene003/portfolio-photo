from django.shortcuts import render
from datetime import date 

def home(request) :
    return render(request, 'site_photo/index.html')

def home(request):
    images = [f"photo{i}.jpg" for i in range(1, 16)]# Génère photo1.jpg à photo15.jpg
    today = date.today().strftime('%d %B %Y')  
    return render(request, 'site_photo/index.html', {"images": images})



# Create your views here.
