from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Conversation, Message, User
from .serializers import ConversationSerializer, MessageSerializer, UserSerializer
# Create your views here.


class ConverstaionViewSet(ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['created_at']  # Enable filtering by created_at
    # Enable search by participant email
    search_fields = ['participants__email']
    ordering_fields = ['created_at']  # Enable ordering by created_at

    def create(request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'message': 'Conversation created successfully',
            'data': response.data
        }, status=status.HTTP_201_CREATED)


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # Filter by conversation or sender
    filterset_fields = ['conversation_id', 'sender_id']
    search_fields = ['content']  # Enable search in message content
    ordering_fields = ['timestamp']  # Enable ordering by timestamp

    def create(request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'message': 'Message created successfully',
            'data': response.data
        }, status=status.HTTP_201_CREATED)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'message': 'User created successfully',
            'data': response.data
        }, status=status.HTTP_201_CREATED)
