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
    todoattendance=models.ManyToManyField(User)
    minutestext=models.TextField()
    
    def __str__(self):
        return self.todoid
 
    class Meta:
        db_table='todominutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcype=models.CharField(max_length=255)
    resourceurl=models.URLField
    resourcedateentered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    
    def __str__(self):
        return self.resourcename
 
    class Meta:
        db_table='resource'
        verbose_name_plural='resources'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.CharField(max_length=255)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventdescription=models.CharField(max_length=255)
    eventuserid=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    
    def __str__(self):
        return self.eventtitle
 
    class Meta:
        db_table='event'
        verbose_name_plural='events'