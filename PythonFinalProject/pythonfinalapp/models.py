from django.db import models
from  django.contrib.auth.models import User

# Create your models here.

class Meeting(models.Model):
    meetingname = models.CharField(max_length=255)
    meetingdate = models.DateField(max_length=255)
    meetingtime = models.TimeField(max_length=255)
    meetinglocation = models.CharField(max_length=255)
    meetingagenda = models.TextField()

    def __str__(self):
        return self.meetingname
 
    class Meta:
        db_table='meeting'
        verbose_name_plural='meetings'
    

class MeetingMinutes(models.Model):
    meetingid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    meetingattendance=models.ManyToManyField(User)
    minutestext=models.TextField()
    
    def __str__(self):
        return self.meetingid
 
    class Meta:
        db_table='meetingminutes'

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