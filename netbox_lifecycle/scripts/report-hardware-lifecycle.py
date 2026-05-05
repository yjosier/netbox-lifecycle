from dcim.choices import DeviceStatusChoices
from dcim.models import Device, Site, Location
from extras.scripts import Script

class HwEolScript(Script):
    class Meta:
        name = "Hardware End-Of-Life Script"
        description = "Report End-Of-Life date of specified devices"

    site_name = ObjectVar(
        description="Site to pull devices from",
        model=Site,
        required=True
    )
    device_status = ChoiceVar(
        DeviceStatusChoices, 
        default=DeviceStatusChoices.STATUS_ACTIVE,
        description="Device Status",
        required=False
    )

    def run(self, data, commit):
        for device in Device.objects.filter(status=data['device_status']):
            for device in Device.objects.filter(site=data['site_name']):
                self.log_info(f"The device type of this device is {device.device_type}", obj=device)
