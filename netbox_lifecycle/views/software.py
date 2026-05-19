from netbox.views.generic import (
    BulkDeleteView,
    BulkEditView,
    BulkImportView,
    ObjectChildrenView,
    ObjectDeleteView,
    ObjectEditView,
    ObjectListView,
    ObjectView,
)
from utilities.views import ViewTab, register_model_view

from netbox_lifecycle.filtersets import SoftwareAssignmentFilterSet, SoftwareFilterSet
from netbox_lifecycle.forms import (
    SoftwareAssignmentBulkEditForm,
    SoftwareAssignmentFilterForm,
    SoftwareAssignmentForm,
    SoftwareAssignmentImportForm,
    SoftwareBulkEditForm,
    SoftwareFilterForm,
    SoftwareForm,
    SoftwareImportForm,
)
from netbox_lifecycle.models import Software, SoftwareAssignment
from netbox_lifecycle.tables import SoftwareAssignmentTable, SoftwareTable

__all__ = (
    'SoftwareAssignmentBulkDeleteView',
    'SoftwareAssignmentBulkEditView',
    'SoftwareAssignmentBulkImportView',
    'SoftwareAssignmentDeleteView',
    'SoftwareAssignmentEditView',
    'SoftwareAssignmentListView',
    'SoftwareAssignmentView',
    'SoftwareAssignmentsView',
    'SoftwareBulkDeleteView',
    'SoftwareBulkEditView',
    'SoftwareBulkImportView',
    'SoftwareDeleteView',
    'SoftwareEditView',
    'SoftwareListView',
    'SoftwareView',
)


@register_model_view(Software, name='list')
class SoftwareListView(ObjectListView):
    queryset = Software.objects.all()
    table = SoftwareTable
    filterset = SoftwareFilterSet
    filterset_form = SoftwareFilterForm


@register_model_view(Software)
class SoftwareView(ObjectView):
    queryset = Software.objects.all()


@register_model_view(Software, 'edit')
class SoftwareEditView(ObjectEditView):
    queryset = Software.objects.all()
    form = SoftwareForm


@register_model_view(Software, 'bulk_edit')
class SoftwareBulkEditView(BulkEditView):
    queryset = Software.objects.all()
    filterset = SoftwareFilterSet
    table = SoftwareTable
    form = SoftwareBulkEditForm


@register_model_view(Software, 'delete')
class SoftwareDeleteView(ObjectDeleteView):
    queryset = Software.objects.all()


@register_model_view(Software, 'bulk_delete')
class SoftwareBulkDeleteView(BulkDeleteView):
    queryset = Software.objects.all()
    filterset = SoftwareFilterSet
    table = SoftwareTable


@register_model_view(Software, 'bulk_import', path='import', detail=False)
class SoftwareBulkImportView(BulkImportView):
    queryset = Software.objects.all()
    model_form = SoftwareImportForm


@register_model_view(Software, 'assignments')
class SoftwareAssignmentsView(ObjectChildrenView):
    template_name = 'netbox_lifecycle/software/assignments.html'
    queryset = Software.objects.all()
    child_model = SoftwareAssignment
    table = SoftwareAssignmentTable
    filterset = SoftwareAssignmentFilterSet
    viewname = None
    actions = {'add': {'add'}, 'edit': {'change'}, 'delete': {'delete'}}
    tab = ViewTab(
        label='Software Assignments',
        badge=lambda obj: SoftwareAssignment.objects.filter(software=obj).count(),
    )

    def get_children(self, request, parent):
        return self.child_model.objects.filter(software=parent)


@register_model_view(SoftwareAssignment, name='list')
class SoftwareAssignmentListView(ObjectListView):
    queryset = SoftwareAssignment.objects.all()
    table = SoftwareAssignmentTable
    filterset = SoftwareAssignmentFilterSet
    filterset_form = SoftwareAssignmentFilterForm


@register_model_view(SoftwareAssignment)
class SoftwareAssignmentView(ObjectView):
    queryset = SoftwareAssignment.objects.all()


@register_model_view(SoftwareAssignment, 'edit')
class SoftwareAssignmentEditView(ObjectEditView):
    queryset = SoftwareAssignment.objects.all()
    form = SoftwareAssignmentForm


@register_model_view(SoftwareAssignment, 'delete')
class SoftwareAssignmentDeleteView(ObjectDeleteView):
    queryset = SoftwareAssignment.objects.all()


@register_model_view(SoftwareAssignment, 'bulk_edit')
class SoftwareAssignmentBulkEditView(BulkEditView):
    queryset = SoftwareAssignment.objects.all()
    filterset = SoftwareAssignmentFilterSet
    table = SoftwareAssignmentTable
    form = SoftwareAssignmentBulkEditForm


@register_model_view(SoftwareAssignment, 'bulk_delete')
class SoftwareAssignmentBulkDeleteView(BulkDeleteView):
    queryset = SoftwareAssignment.objects.all()
    filterset = SoftwareAssignmentFilterSet
    table = SoftwareAssignmentTable


@register_model_view(SoftwareAssignment, 'bulk_import', path='import', detail=False)
class SoftwareAssignmentBulkImportView(BulkImportView):
    queryset = SoftwareAssignment.objects.all()
    model_form = SoftwareAssignmentImportForm
