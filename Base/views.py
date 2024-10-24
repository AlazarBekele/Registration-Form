from django.shortcuts import render
from .models import WelcomePage

# Create your views here.

def index (request):

  front_Img = WelcomePage.objects.filter().order_by('-title')[:2]

  context = {

    'front_Img' : front_Img

  }
  
  return render (request, 'index.html', context=context)