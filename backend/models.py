from django.db import models

# Create your models here.

class EventHappened(models.Model):
    title = models.CharField(max_length=255)
    information = models.TextField()
    image = models.ImageField(upload_to='events_images/')
class UpcommingEvents(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    registration =  models.URLField()
class Team(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    information = models.TextField()
    image = models.ImageField(upload_to='team_images/')




