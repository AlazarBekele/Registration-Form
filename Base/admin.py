from django.contrib import admin
from .models import WelcomePage, RegisterUpload

# Register your models here.

admin.site.register (WelcomePage)
admin.site.register (RegisterUpload)