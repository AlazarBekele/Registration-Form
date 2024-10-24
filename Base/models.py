from django.db import models

# Create your models here.

class WelcomePage (models.Model):

  title = models.CharField (max_length=20)
  picture = models.ImageField (upload_to='photo/')

  def __str__(self) -> str:
    return self.title
  

class RegisterUpload (models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  dob = models.DateField (auto_now=False, auto_now_add=False)
  school = models.CharField(max_length=50)
  grade = models.IntegerField()
  email = models.CharField(max_length=40)
  address = models.CharField(max_length=70)
  id_number = models.IntegerField()

  def __str__(self) -> str:
    return self.first_name + " " + self.last_name