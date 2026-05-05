from dcim.choices import DeviceStatusChoices
from dcim.models import Device, DeviceType, Site
from extras.scripts import *

class HwEolScript(Script):
    class Meta(Script.Meta):
        name = "Hardware End-Of-Life Script"
        description = "Report End-Of-Life date of specified devices"
        field_order = ['site_name', 'device_status']

    site = ObjectVar(
        description="Site to pull devices from",
        model=Site,
        required=True
    )
    device_status = ChoiceVar(
        DeviceStatusChoices, 
        default=DeviceStatusChoices.STATUS_ACTIVE,
        description="Device Status",
        required=True
    )

    def run(self, data, commit):
        output = ['name,model,eol']
        # self.log_info(f"In run function")
        # self.log_info(f"Device status from form = {data['device_status']}")
        for device in Device.objects.filter(status=data['device_status']):
            # self.log_info(f"In for loop")
            # self.log_info(f"Device site name = {device.site.name}")
            # self.log_info(f"Device site name from form = {data['site']}")
            if device.site == data['site']:
                #self.log_info(f"The device type of this device is {device.device_type}", obj=device)
                eol = getattr(device.device_type.hardware_lifecycle.first(), 'end_of_support', None)
                if eol:
                    self.log_info(f"The EoL for {device} is : {eol}", obj=device)
                else:
                    self.log_info(f"The EoL for {device} is undefined.", obj=device)
                attrs = [
                    device.name,
                    device.device_type.name,
                    eol
                ]
                output.append(','.join(attrs))
        return '\n'.join(output)

