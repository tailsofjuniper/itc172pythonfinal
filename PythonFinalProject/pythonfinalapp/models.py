from django.db import models
from  django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    todoname = models.CharField(max_length=255)
    tododate = models.DateField(max_length=255)
    todotime = models.TimeField(max_length=255)
    todolocation = models.CharField(max_length=255)

    def __str__(self):
        return self.todoname
 
    class Meta:
        db_table='todo'
        verbose_name_plural='todos'
    

class Details(models.Model):
    todoid=models.ForeignKey(Todo, on_delete=models.DO_NOTHING)
    todoname=models.ForeignKey(Todo, on_delete=models.DO_NOTHING)
    todoagenda=models.TextField()
    
    def __str__(self):
        return self.todoid
 
    class Meta:
        db_table='tododetails'