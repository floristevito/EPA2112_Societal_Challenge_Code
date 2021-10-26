from rest_framework import serializers

from .models import Feedback

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id','age', 'frequency', 'reasonOfVisit', 'stars', 'feedback', 'qr_name')