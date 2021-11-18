from django.db import models

# Create your models here.
class Feedback(models.Model):
    age = models.IntegerField(null=True, blank=True, default=None)
    frequency = models.CharField(max_length = 100, null=True, blank=True, default=None)
    reasonOfVisit = models.CharField(max_length = 100, null=True, blank=True, default=None)
    stars = models.CharField(max_length = 100, null=True, blank=True, default=None)
    feedback = models.CharField(max_length = 1000, null=True, blank=True, default=None)
    safety = models.IntegerField(null=True, blank=True, default=None)
    qr_id= models.CharField(max_length = 100, null=True, blank=True, default=None)
    
    def __str__(self):
        return self.qr_id
