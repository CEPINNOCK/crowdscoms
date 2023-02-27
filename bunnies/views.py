# Import the necessary modules
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from bunnies.models import Bunny, RabbitHole
from bunnies.permissions import RabbitHolePermissions
from bunnies.serializers import BunnySerializer, RabbitHoleSerializer


class RabbitHoleViewSet(viewsets.ModelViewSet):
    """
    Class base view for viewing and editing rabbit holes instances.
    """
    serializer_class = RabbitHoleSerializer
    permission_classes = (IsAuthenticated, RabbitHolePermissions)
    queryset = RabbitHole.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Override the create method to add custom logic.
        """
        return super().create(request, *args, **kwargs)

    def filter_queryset(self, queryset):
        """
        Override the filter_queryset method to add custom filtering logic.
        """
        return queryset


class BunnyViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing bunny instances.
    """
    serializer_class = BunnySerializer
    permission_classes = (IsAuthenticated,)
    queryset = Bunny.objects.all()
