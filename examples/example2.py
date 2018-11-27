from vsensortag.vsensortag import VirtualSensorTag
import time
	
    
sensortag = VirtualSensorTag("172.29.156.35", 1883)
sensortag.enable()

try:
    while True:
        print(sensortag.read_accelerometer_sensor())
        print(sensortag.read_humidity_sensor())
        print(sensortag.read_magnetometer_sensor())
        print(sensortag.read_barometer_sensor())
        print(sensortag.read_gyroscope_sensor())
        print(sensortag.read_light_sensor())
        print(sensortag.read_battery_sensor())
        print()
        time.sleep(1)

except KeyboardInterrupt:
    sensortag.disable()