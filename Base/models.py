from django.db import models

# Create your models here.

class WelcomePage (models.Model):

  title = models.CharField (max_length=20)
  picture = models.ImageField (upload_to='photo/')

  def __str__(self) -> str:
    return self.title