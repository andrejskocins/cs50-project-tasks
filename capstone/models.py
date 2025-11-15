from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Task(models.Model):
    author = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)    
    title = models.CharField(max_length=128)
    description = models.CharField(blank=True)
    due_date = models.DateField(blank=True)
    completed = models.BooleanField(default=False)
    start_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title