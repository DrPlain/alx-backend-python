from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Conversation, Message, User
from .serializers import ConversationSerializer, MessageSerializer, UserSerializer
# Create your views here.


class ConverstaionViewset(ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer


class MessageViewset(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
