from django.db import models

# Create your models here.
class Event(models.Model):
    banner = models.ImageField()
    event_name = models.CharField(max_length=40)
    venue = models.CharField(max_length=40)
    date = models.DateField()
    time = models.TimeField()
    charges = models.CharField(max_length=40)
    contact = models.IntegerField()
    description=models.CharField(max_length=1000000)

    def __str__(self):
        return self.event_name

class Comment(models.Model):
    event_name = models.ForeignKey(Event, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=40)
    comment=models.CharField(max_length=40)

    def __str__(self):
        return self.user_name

