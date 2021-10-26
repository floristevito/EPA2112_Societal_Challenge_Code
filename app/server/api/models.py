from django.db import models

# Create your models here.
class Feedback(models.Model):
    age = models.IntegerField()
    frequency = models.CharField(max_length = 100)
    reasonOfVisit = models.CharField(max_length = 100)
    stars = models.CharField(max_length = 100)
    feedback = models.CharField(max_length = 1000)
    qr_name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.qr_name
