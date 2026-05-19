from dcim.api.serializers_.devices import DeviceSerializer
from dcim.api.serializers_.manufacturers import ManufacturerSerializer
from netbox.api.serializers import NetBoxModelSerializer
from rest_framework import serializers
from virtualization.api.serializers_.virtualmachines import VirtualMachineSerializer

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
    end_of_software_maintenance = serializers.DateField(required=False, allow_null=True)
    end_of_security_maintenance = serializers.DateField(required=False, allow_null=True)
    end_of_life = serializers.DateField(required=False, allow_null=True)

    class Meta:
        model = Software
        fields = (
            'url',
            'id',
            'display',
            'name',
            'manufacturer',
            'end_of_software_maintenance',
            'end_of_security_maintenance',
            'end_of_life',
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
    manufacturer = ManufacturerSerializer(nested=True)
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
            'manufacturer',
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
            'manufacturer',
            'software',
            'device',
            'virtual_machine',
        )
