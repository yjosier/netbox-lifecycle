from dcim.api.serializers_.devices import DeviceSerializer
from dcim.api.serializers_.manufacturers import ManufacturerSerializer
from netbox.api.serializers import NetBoxModelSerializer
from rest_framework import serializers
from virtualization.api.serializers_.virtualmachines import VirtualMachineSerializer

from netbox_lifecycle.api._serializers.vendor import VendorSerializer
from netbox_lifecycle.models import Software, SoftwareAssignment

__all__ = (
    'SoftwareAssignmentSerializer',
    'SoftwareSerializer',
)


class SoftwareSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_lifecycle-api:software-detail'
    )
    manufacturer = ManufacturerSerializer(nested=True)

    class Meta:
        model = Software
        fields = (
            'url',
            'id',
            'display',
            'name',
            'manufacturer',
            'description',
            'comments',
            'tags',
            'custom_fields',
        )
        brief_fields = (
            'url',
            'id',
            'display',
            'name',
        )


class SoftwareAssignmentSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_lifecycle-api:softwareassignment-detail'
    )
    software = SoftwareSerializer(nested=True)
    vendor = VendorSerializer(nested=True)
    device = DeviceSerializer(nested=True, required=False, allow_null=True)
    virtual_machine = VirtualMachineSerializer(
        nested=True, required=False, allow_null=True
    )

    class Meta:
        model = SoftwareAssignment
        fields = (
            'url',
            'id',
            'display',
            'vendor',
            'software',
            'device',
            'virtual_machine',
            'quantity',
            'description',
            'comments',
            'tags',
            'custom_fields',
        )
        brief_fields = (
            'url',
            'id',
            'display',
            'vendor',
            'software',
            'device',
            'virtual_machine',
        )
