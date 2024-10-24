from django.shortcuts import render
from .models import RegisterUpload, WelcomePage
from .form import StudentForms
from django.contrib import messages

# Create your views here.

def index (request):

  front_Img = WelcomePage.objects.filter().order_by('-title')[:2]

  context = {

    'front_Img' : front_Img

  }
  
  return render (request, 'index.html', context=context)

def register (request):

  form = StudentForms(request.POST or None)

  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request, 'Successfully Registered!')
      form = RegisterUpload()

  context = {
    'form' : form
  }

  return render (request, 'MainRegister.html', context=context)