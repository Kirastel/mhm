from rest_framework import viewsets

from main.models import Entity
from main.serializers import EntitySerializer


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
