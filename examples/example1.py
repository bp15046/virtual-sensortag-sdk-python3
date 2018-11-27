from vsensortag.vsensortag import VirtualSensorTag
import time
	
    
sensortag = VirtualSensorTag("172.29.156.35", 1883)
sensortag.enable()

try:
    while True:
        print("accel x     :", sensortag.get_accel_x())
        print("accel y     :", sensortag.get_accel_y())
        print("accel z     :", sensortag.get_accel_z())
        print("humidity    :", sensortag.get_humidity())
        print("mag x       :", sensortag.get_mag_x())
        print("mag y       :", sensortag.get_mag_y())
        print("mag z       :", sensortag.get_mag_z())
        print("temperature :", sensortag.get_temperature())
        print("pressure    :", sensortag.get_pressure())
        print("gyro x      :", sensortag.get_gyro_x())
        print("gyro y      :", sensortag.get_gyro_y())
        print("gyro z      :", sensortag.get_gyro_z())
        print("light       :", sensortag.get_light())
        print("battery     :", sensortag.get_battery())
        print()
	
        time.sleep(1)

except KeyboardInterrupt:
    sensortag.disable()