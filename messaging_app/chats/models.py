from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ROLE_CHOICES = [
        ('guest', 'guest'),
        ('host', 'host'),
        ('admin', 'admin')
    ]
    user_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']

    class Meta:
        indexes = [
            models.Index(fields=['email'])
        ]

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Conversation(models.Model):
    conversation_id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    participants = models.ManyToManyField(
        User, related_name='conversations')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.conversation_id} created at {self.created_at}"


class Message(models.Model):
    message_id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    sender_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='messages')
    conversation_id = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name='messages')
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['sent_at'])
        ]

    def __str__(self):
        return f"Message from {self.sender.email} at {self.sent_at}"
