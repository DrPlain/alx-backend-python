from rest_framework import routers
from rest_framework_nested.routers import NestedDefaultRouter
from django.urls import path, include
from .views import ConversationViewSet, MessageViewSet, UserViewSet

router = routers.DefaultRouter()

router.register(r'conversations', ConversationViewSet,
                basename='conversations')
router.register(r'messages', MessageViewSet, basename='messages')
router.register(r'users', UserViewSet, 'users')

# Nested router for messages within a conversation
nested_router = NestedDefaultRouter(
    router, r'conversations', lookup='conversation_id')
nested_router.register(r'messages', MessageViewSet,
                       basename='conversation-messages')

urlpatterns = []
urlpatterns += router.urls
urlpatterns += nested_router.urls
