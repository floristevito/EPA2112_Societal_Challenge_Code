from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import Feedback


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all().order_by('qr_id')
    serializer_class = HeroSerializer
    http_method_names = ['post']