from rest_framework import routers
from api.views import NotificationViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'notification', NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]