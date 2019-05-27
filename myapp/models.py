from django.db import models

# Create your models here.

class TodoItem(models.Model):
    todo_item = models.CharField(max_length=128)
    todo_date = models.DateField()
    bFinish = models.BooleanField()
    add_time = models.DateTimeField(auto_now_add=True)