from rest_framework import routers
from django.urls import path, include
from .views import ConversationViewSet, MessageViewSet, UserViewSet

router = routers.DefaultRouter()

router.register(r'conversation', ConversationViewSet)
router.register(r'message', MessageViewSet)
router.register(r'user', UserViewSet)

urlpatterns = router.urls
