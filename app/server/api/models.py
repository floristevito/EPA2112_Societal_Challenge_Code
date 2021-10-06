from django.db import models

# Create your models here.
class Feedback(models.Model):
    qr_name = models.CharField(max_length = 100)
    age = models.IntegerField()
    lat = models.FloatField()
    long = models.FloatField()
    feedback = models.CharField(max_length = 1000)
    
    def __str__(self):
        return self.qr_name