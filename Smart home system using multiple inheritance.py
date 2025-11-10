#Challenge: Smart Home Device System
# Creating a smart home system that models devices with different capabilities like turning on/off, connecting to Wi-Fi, and monitoring temperature- Using multiple inheritance

class Device:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
    
    def device_info(self):
        print(f"Device: {self.name} | Brand: {self.brand}")


class PowerControl:
    def turn_on(self):
        print(f"{self.name} is now ON")

    def turn_off(self):
        print(f"{self.name} is now OFF")


class WiFiEnabled:
    def __init__(self,ssid):
        self.ssid = ssid
    def connect_wifi(self):
        print(f"{self.name} connect to WiFi network '{self.ssid}'")
    
class TemperatureMonitor:
    def read_temperature(self):
        print(f"{self.name} temperature is 24'C.")

class SmartLight(Device, PowerControl, WiFiEnabled):
    def __init__(self, name, brand, ssid):
        Device.__init__(self, name, brand)
        WiFiEnabled.__init__(self,ssid)


class SmartThermostat(Device, PowerControl, WiFiEnabled, TemperatureMonitor):
    def __init__(self,name, brand, ssid):
        Device.__init__(self, name, brand)
        WiFiEnabled.__init__(self,ssid)

light = SmartLight("Living Room Light", "Philips", "Home WiFi")
light.device_info()
light.turn_on()
light.turn_off()
light.connect_wifi()




thermostat = SmartThermostat("Nest thermostat", "Google", "Home WiFi")

thermostat.device_info()
thermostat.turn_off()
thermostat.turn_on()
thermostat.connect_wifi()
thermostat.read_temperature()