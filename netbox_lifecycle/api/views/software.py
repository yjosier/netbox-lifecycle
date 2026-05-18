from netbox.api.viewsets import NetBoxModelViewSet

from netbox_lifecycle.api.serializers import (
    SoftwareAssignmentSerializer,
    SoftwareSerializer,
)
from netbox_lifecycle.filtersets import SoftwareAssignmentFilterSet, SoftwareFilterSet
from netbox_lifecycle.models import Software, SoftwareAssignment

__all__ = ('SoftwareAssignmentViewSet', 'SoftwareViewSet')


class SoftwareViewSet(NetBoxModelViewSet):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
    filterset_class = SoftwareFilterSet


class SoftwareAssignmentViewSet(NetBoxModelViewSet):
    queryset = SoftwareAssignment.objects.all()
    serializer_class = SoftwareAssignmentSerializer
    filterset_class = SoftwareAssignmentFilterSet
