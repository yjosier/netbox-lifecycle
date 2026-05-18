import django_tables2 as tables
from django.utils.translation import gettext as _
from netbox.tables import NetBoxTable

from netbox_lifecycle.models import Software, SoftwareAssignment

__all__ = (
    'SoftwareAssignmentTable',
    'SoftwareTable',
)


class SoftwareTable(NetBoxTable):
    name = tables.Column(
        verbose_name=_('Name'),
        linkify=True,
    )
    manufacturer = tables.Column(verbose_name=_('Manufacturer'), linkify=True)

    class Meta(NetBoxTable.Meta):
        model = Software
        fields = (
            'pk',
            'name',
            'description',
            'comments',
        )
        default_columns = (
            'pk',
            'name',
        )


class SoftwareAssignmentTable(NetBoxTable):
    software = tables.Column(verbose_name=_('Software'), linkify=True)
    vendor = tables.Column(verbose_name=_('Vendor'), linkify=True)
    device = tables.Column(verbose_name=_('Device'), linkify=True)
    virtual_machine = tables.Column(verbose_name=_('Virtual Machine'), linkify=True)

    class Meta(NetBoxTable.Meta):
        model = SoftwareAssignment
        fields = (
            'pk',
            'software',
            'vendor',
            'device',
            'virtual_machine',
            'quantity',
            'description',
            'comments',
        )
        default_columns = ('pk', 'software', 'vendor', 'device', 'virtual_machine')
