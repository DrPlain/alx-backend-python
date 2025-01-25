from rest_framework import serializers
from .models import MessageHistory, Message


class MessageHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageHistory
        fields = ['id', 'message', 'old_content', 'edited_by', 'edited_at']
        read_only_fields = ['edited_by', 'edited_at']


class MessagingSerializer(serializers.ModelSerializer):
    edit_history = MessageHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'content',
                  'timestamp', 'edited', 'edit_history']
        read_only_fields = ['edited']
