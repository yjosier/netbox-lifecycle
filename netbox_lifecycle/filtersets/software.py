import django_filters
from dcim.models import Device, Manufacturer
from django.db.models import Q
from django.utils.translation import gettext as _
from netbox.filtersets import NetBoxModelFilterSet
from virtualization.models import VirtualMachine

from netbox_lifecycle.models import Software, SoftwareAssignment

__all__ = (
    'SoftwareAssignmentFilterSet',
    'SoftwareFilterSet',
)


class SoftwareFilterSet(NetBoxModelFilterSet):
    manufacturer_id = django_filters.ModelMultipleChoiceFilter(
        field_name='software__manufacturer',
        queryset=Manufacturer.objects.all(),
        label=_('Manufacturer'),
    )
    manufacturer = django_filters.ModelMultipleChoiceFilter(
        field_name='software__manufacturer__slug',
        queryset=Manufacturer.objects.all(),
        to_field_name='slug',
        label=_('Manufacturer (Slug)'),
    )

    class Meta:
        model = Software
        fields = (
            'id',
            'q',
            'name',
        )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = Q(manufacturer__name__icontains=value) | Q(name__icontains=value)
        return queryset.filter(qs_filter).distinct()


class SoftwareAssignmentFilterSet(NetBoxModelFilterSet):
    software_id = django_filters.ModelMultipleChoiceFilter(
        field_name='software',
        queryset=Software.objects.all(),
        label=_('Software'),
    )
    software = django_filters.ModelMultipleChoiceFilter(
        field_name='software__name',
        queryset=Software.objects.all(),
        to_field_name='name',
        label=_('Software'),
    )
    manufacturer_id = django_filters.ModelMultipleChoiceFilter(
        field_name='manufacturer',
        queryset=Manufacturer.objects.all(),
        label=_('Manufacturer'),
    )
    manufacturer = django_filters.ModelMultipleChoiceFilter(
        field_name='manufacturer__slug',
        queryset=Manufacturer.objects.all(),
        to_field_name='slug',
        label=_('Manufacturer (Slug)'),
    )
    device_id = django_filters.ModelMultipleChoiceFilter(
        field_name='device',
        queryset=Device.objects.all(),
        label=_('Device'),
    )
    device = django_filters.ModelMultipleChoiceFilter(
        field_name='device__name',
        queryset=Device.objects.all(),
        to_field_name='name',
        label=_('Device'),
    )
    virtual_machine_id = django_filters.ModelMultipleChoiceFilter(
        field_name='virtual_machine',
        queryset=VirtualMachine.objects.all(),
        label=_('Virtual Machine'),
    )
    virtual_machine = django_filters.ModelMultipleChoiceFilter(
        field_name='virtual_machine__name',
        queryset=VirtualMachine.objects.all(),
        to_field_name='name',
        label=_('Virtual Machine'),
    )

    class Meta:
        model = SoftwareAssignment
        fields = (
            'id',
            'q',
        )

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = (
            Q(software__manufacturer__name__icontains=value)
            | Q(software__name__icontains=value)
            | Q(manufacturer__name__icontains=value)
            | Q(device__name__icontains=value)
            | Q(virtual_machine__name__icontains=value)
        )
        return queryset.filter(qs_filter).distinct()
