from rest_framework.viewsets import ModelViewSet

from core.models import autor 
from core.serializers.autor import autorSerializer

class autorViewSet(ModelViewSet):
    queryset = autor.objects.all()
    serializer_class = autorSerializer