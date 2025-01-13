from django.test import TestCase
from chats.models import User
from .models import Message, Notification


class MessageNotificationTestCase(TestCase):

    def setUp(self):
        """
        Set up test data for the tests.
        """
        # Create two users
        self.sender = User.objects.create_user(
            email='sender@gmail.com', password='password123')
        self.receiver = User.objects.create_user(
            email='receiver@gmail.com', password='password123')

    def test_message_creation_creates_notification(self):
        """
        Test that creating a message also creates a notification for the receiver.
        """
        # Create a message
        message = Message.objects.create(
            sender=self.sender, receiver=self.receiver, content="Test message")

        # Check if a notification was created
        notifications = Notification.objects.filter(
            user=self.receiver, message=message)
        self.assertEqual(notifications.count(), 1)

        # Verify the notification details
        notification = notifications.first()
        self.assertEqual(notification.notification_type, 'Message')
        self.assertFalse(notification.is_read)  # Should be unread initially

    def test_no_duplicate_notifications(self):
        """
        Ensure that creating a message doesn't result in duplicate notifications.
        """
        # Create a message
        Message.objects.create(
            sender=self.sender, receiver=self.receiver, content="Another test message")

        # Create the same message again
        message = Message.objects.create(
            sender=self.sender, receiver=self.receiver, content="Another test message")

        # Check that only one notification exists for the receiver and this message
        notifications = Notification.objects.filter(
            user=self.receiver, message=message)
        self.assertEqual(notifications.count(), 1)

    def test_no_notification_for_sender(self):
        """
        Ensure that no notification is created for the sender of the message.
        """
        # Create a message
        Message.objects.create(
            sender=self.sender, receiver=self.receiver, content="Hello!")

        # Check that no notification exists for the sender
        sender_notifications = Notification.objects.filter(user=self.sender)
        self.assertEqual(sender_notifications.count(), 0)
