from project.software.express_software import ExpressSoftware
from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware


class System:
    _hardware = []
    _software = []
    _memory_used = 0
    _capacity_used = 0

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware_obj = ''
        for el in System._hardware:
            if el.name == hardware_name:
                hardware_obj = el

        if hardware_obj == '':
            return "Hardware does not exist"

        try:
            app = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware_obj.install(app)
            System._software.append(app)
            System._capacity_used += app.capacity_consumption
            System._memory_used += app.memory_consumption
        except Exception:
            return "Software cannot be installed"

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        hardware_obj = ''
        for el in System._hardware:
            if el.name == hardware_name:
                hardware_obj = el

        if hardware_obj == '':
            return "Hardware does not exist"

        try:
            app = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware_obj.install(app)
            System._software.append(app)
            System._capacity_used += app.capacity_consumption
            System._memory_used += app.memory_consumption
        except Exception:
            return "Software cannot be installed"

    @staticmethod
    def release_software_component(hardware_name, software_name):
        hardware_obj = ''
        for el in System._hardware:
            if el.name == hardware_name:
                hardware_obj = el
                break

        software_obj = ''
        for el in System._software:
            if el.name == software_name:
                software_obj = el
                break

        if not software_obj == '' and not hardware_obj == '':
            hardware_obj.uninstall(software_obj)
            System._software.remove(software_obj)
            System._capacity_used -= software_obj.capacity_consumption
            System._memory_used -= software_obj.memory_consumption
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {int(System._memory_used)} / {int(sum([el.memory for el in System._hardware]))}\n" \
               f"Total Capacity Taken: {int(System._capacity_used)} / {int(sum([el.capacity for el in System._hardware]))}"

    @staticmethod
    def system_split():
        sep = ", "
        result = ''
        for el in System._hardware:
            if len(el.software_components) == 0:
                result += f"Hardware Component - {el.name}\n" \
                          f"Express Software Components: {len([app for app in el.software_components if app.__class__.__name__ == 'ExpressSoftware'])}\n" \
                          f"Light Software Components: {len([app for app in el.software_components if app.__class__.__name__ == 'LightSoftware'])}\n" \
                          f"Memory Usage: {int(sum([app.memory_consumption for app in el.software_components]))} / {int(el.memory)}\n" \
                          f"Capacity Usage: {int(sum([app.capacity_consumption for app in el.software_components]))} / {int(el.capacity)}\n" \
                          f"Type: {el.type}\n" \
                          f"Software Components: None"
            else:
                result += f"Hardware Component - {el.name}\n" \
                       f"Express Software Components: {len([app for app in el.software_components if app.__class__.__name__ == 'ExpressSoftware'])}\n" \
                       f"Light Software Components: {len([app for app in el.software_components if app.__class__.__name__ == 'LightSoftware'])}\n" \
                       f"Memory Usage: {int(sum([app.memory_consumption for app in el.software_components]))} / {int(el.memory)}\n" \
                       f"Capacity Usage: {int(sum([app.capacity_consumption for app in el.software_components]))} / {int(el.capacity)}\n" \
                       f"Type: {el.type}\n" \
                       f"Software Components: {sep.join([app.name for app in el.software_components])}"

        return result


# 117/150
# 150/150