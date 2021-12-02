from rest_framework.viewsets import ModelViewSet
from api.serializers import NotificationSerializer
from api.models import Notification
from oauth2_provider.contrib.rest_framework import TokenHasResourceScope
class NotificationViewSet(ModelViewSet):

    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    permission_classes = [TokenHasResourceScope]
    http_method_names = ['get', 'patch', 'post']
    # required_scopes = ('read','write')

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset