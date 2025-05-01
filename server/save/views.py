from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import Save
from .serializers import SaveSerializer
from .permissions import IsSaveOwner
from django_filters.rest_framework import DjangoFilterBackend

class SaveViewSet(ModelViewSet):
    serializer_class = SaveSerializer
    http_method_names = ['get', 'post', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tag']
    
    def get_queryset(self):
        if (self.action == 'list'):
            return Save.objects.filter(user=self.request.user) # return all saves of current user in /saves/
        
        return Save.objects.all()
    
    def get_permissions(self):
        if self.action == 'destroy':
            return [permissions.IsAuthenticated(), IsSaveOwner()]
        
        return [permissions.IsAuthenticated()]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
