'''
from django.db import models

# Create your models here.
class Task(models.Model):
  title = models.CharField(max_length=200)
  complete = models.BooleanField(default=False)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

'''

'''
# models.py
from django.db import models
from django.contrib.auth import get_user_model

class Task(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

'''

# models.py
from django.db import models
from django.contrib.auth import get_user_model

class Task(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    deadline = models.DateField(null=True, blank=True)  # Add the deadline field

    def __str__(self):
        return self.title