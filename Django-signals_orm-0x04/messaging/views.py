from django.shortcuts import render
from .serializers import MessageHistorySerializer, MessagingSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Message
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class MessageViewset(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessagingSerializer
    # permission_classes = [IsAuthenticated]
