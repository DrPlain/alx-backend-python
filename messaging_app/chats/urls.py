from rest_framework import routers
from django.urls import path, include
from .views import ConverstaionViewSet, MessageViewSet, UserViewSet

router = routers.DefaultRouter()

router.register(r'conversation', ConverstaionViewSet)
router.register(r'message', MessageViewSet)
router.register(r'user', UserViewSet)

urlpatterns = router.urls
