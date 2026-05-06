from dcim.choices import DeviceStatusChoices
from dcim.models import Device
from netbox_lifecycle.models import SupportContractAssignment
from netbox_lifecycle.constants import CONTRACT_STATUS_ACTIVE
from extras.scripts import *
from datetime import datetime
import csv
import io

# self.log_info(f"Device site name = {device.site.name}")
# self.log_info(f"Device site name from form = {data['site']}")
# self.log_info(f"Device status from form = {data['device_status']}")
# self.log_info(f"The device type of this device is {device.device_type}", obj=device)


class Hwend_of_lifeScript(Script):
    class Meta(Script.Meta):
        name = "Spending forecast of devices"
        description = "Report spending forecast for infrastructure"
        field_order = ['device_status']

    device_status = ChoiceVar(
        DeviceStatusChoices, 
        default=DeviceStatusChoices.STATUS_ACTIVE,
        description="Device Status",
        required=True
    )

    def run(self, data, commit):
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow([
            'Device_Site', 'Device_Name', 'Device_Type', 'Device_Role',
            'End_of_Sale', 'End_of_Maintenance', 'End_of_Security', 'End_of_Support',
            'Support_Contract', 'End_of_Contract', 'Est_Renewal_Price',
        ])

        devices = Device.objects.filter(status=data['device_status']).select_related('device_type', 'role', 'site')

        for device in devices:
            lifecycle = device.device_type.hardware_lifecycle.first()

            def date_to_string(d):
                return d.strftime("%d/%m/%Y") if d else ''

            renewal_price = device.device_type.cf.get('Estimated_Renewal_Price', '') if hasattr(device.device_type, 'cf') else ''

            active_assignments = [
                assignment for assignment in SupportContractAssignment.objects.filter(device=device).select_related('contract')
                if assignment.status == CONTRACT_STATUS_ACTIVE
            ]

            contract_id = active_assignments[0].contract.contract_id if active_assignments else ''
            contract_end = active_assignments[0].end_date if active_assignments and active_assignments[0].end_date else ''

            writer.writerow([
                device.site.name,
                device.name or 'Unamed device',
                device.device_type.model,
                device.role.name if device.role else '',
                date_to_string(getattr(lifecycle, 'end_of_sale', None)),
                date_to_string(getattr(lifecycle, 'end_of_maintenance', None)),
                date_to_string(getattr(lifecycle, 'end_of_security', None)),
                date_to_string(getattr(lifecycle, 'end_of_support', None)),
                contract_id,
                date_to_string(contract_end),
                renewal_price
            ])

        return output.getvalue()