from rest_framework.routers import DefaultRouter
from .views import ConverstaionViewset, MessageViewset, UserViewset

router = DefaultRouter()

router.register(r'conversation', ConverstaionViewset)
router.register(r'message', MessageViewset)
router.register(r'user', UserViewset)

urlpatterns = router.urls
