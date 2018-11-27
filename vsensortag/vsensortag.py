from vsensortag import vsensor
import ast
import time


class VirtualSensorTag():
	def __init__(self, addr, port):
		self.accelerometer_sensor = vsensor.VirtualAccelerometerSensor(addr, port)
		self.humidity_sensor      = vsensor.VirtualHumiditySensor(addr, port)
		self.magnetometer_sensor  = vsensor.VirtualMagnetometerSensor(addr, port)
		self.barometer_sensor     = vsensor.VirtualBarometerSensor(addr, port)
		self.gyroscope_sensor     = vsensor.VirtualGyroscopeSensor(addr, port)
		self.light_sensor         = vsensor.VirtualLightSensor(addr, port)
		self.battery_sensor       = vsensor.VirtualBatterySensor(addr, port)

	def enable(self):
		self.accelerometer_sensor.enable("prototyping_env/sensor/sensortag/accelerometer_sensor")
		self.humidity_sensor.enable("prototyping_env/sensor/sensortag/humidity_sensor")
		self.magnetometer_sensor.enable("prototyping_env/sensor/sensortag/magnetometer_sensor")
		self.barometer_sensor.enable("prototyping_env/sensor/sensortag/barometer_sensor")
		self.gyroscope_sensor.enable("prototyping_env/sensor/sensortag/gyroscope_sensor")
		self.light_sensor.enable("prototyping_env/sensor/sensortag/light_sensor")
		self.battery_sensor.enable("prototyping_env/sensor/sensortag/battery_sensor")

	def disable(self):
		self.accelerometer_sensor.disable()
		self.humidity_sensor.disable()
		self.magnetometer_sensor.disable()
		self.barometer_sensor.disable()
		self.gyroscope_sensor.disable()
		self.light_sensor.disable()
		self.battery_sensor.disable()

	def read_accelerometer_sensor(self):
		pyaload = self.accelerometer_sensor.read().decode('utf-8')
		return ast.literal_eval(payload)
	
	def read_humidity_sensor(self):
		payload = self.humidity_sensor.read().decode('utf-8')
		return ast.literal_eval(payload)
	
	def read_magnetometer_sensor(self):
		payload = self.magnetometer_sensor.read().decode('utf-8')
		return ast.literal_eval(payload)
	
	def read_barometer_sensor(self):
		payload = self.barometer_sensor.read().decode('utf-8')
		return ast.literal_eval()
	
	def read_gyroscope_sensor(self):
		payload = self.gyroscope_sensor.read().decode('utf-8')
		return ast.literal_eval()

	def read_light_sensor(self):
		payload = self.light_sensor.read().decode('utf-8')
		return ast.literal_eval()
	
	def read_battery_sensor(self):
		payload = self.battery_sensor.read().decode('utf-8')
		return ast.literal_eval()

	def get_accel_x(self):
		payload = self.accelerometer_sensor.read().decode('utf-8')
		payload_dit = ast.literal_eval(payload)
		return payload_dit["accelerometer_sensor"]["accel_x"]

	def get_accel_y(self):
		payload = self.accelerometer_sensor.read().decode('utf-8')
		payload_dit = ast.literal_eval(payload)
		return payload_dit["accelerometer_sensor"]["accel_y"]

	def get_accel_z(self):
		payload = self.accelerometer_sensor.read().decode('utf-8')
		payload_dit = ast.literal_eval(payload)
		return payload_dit["accelerometer_sensor"]["accel_z"]
	
	def get_humidity(self):
		payload = self.humidity_sensor.read().decode('utf-8')
		payload_dit = ast.literal_eval(payload)
		return payload_dit["humidity_sensor"]["humidity"]
	
	def get_mag_x(self):
		payload = self.magnetometer_sensor.read().decode('utf-8')
		payload_dit = ast.literal_eval(payload)
		return payload_dit["magnetometer_sensor"]["mag_x"]
	
	def get_mag_y(self):
		payload = self.magnetometer_sensor.read().decode('utf-8')
		payload_dit = ast.literal_eval(payload)
		return payload_dit["magnetometer_sensor"]["mag_y"]

	def get_mag_z(self):
		payload = self.magnetometer_sensor.read().decode('utf-8')
		payload_dit = ast.literal_eval(payload)
		return payload_dit["magnetometer_sensor"]["mag_z"]

	def get_temperature(self):
		payload = self.barometer_sensor.read().decode('utf-8')
		payload_dit = ast.literal_eval(payload)
		return payload_dit["barometer_sensor"]["temperature"]

	def get_pressure(self):
		payload = self.barometer_sensor.read().decode('utf-8')
		payload_dit = ast.literal_eval(payload)
		return payload_dit["barometer_sensor"]["pressure"]

	def get_gyro_x(self):
		payload = self.gyroscope_sensor.read().decode('utf-8')
		payload_dit = ast.literal_eval(payload)
		return payload_dit["gyroscope_sensor"]["gyro_x"]

	def get_gyro_y(self):
		payload = self.gyroscope_sensor.read().decode('utf-8')
		payload_dit = ast.literal_eval(payload)
		return payload_dit["gyroscope_sensor"]["gyro_y"]
	
	def get_gyro_z(self):
		payload = self.gyroscope_sensor.read().decode('utf-8')
		payload_dit = ast.literal_eval(payload)
		return payload_dit["gyroscope_sensor"]["gyro_z"]
	
	def get_light(self):
		payload = self.light_sensor.read().decode('utf-8')
		payload_dit = ast.literal_eval(payload)
		return payload_dit["light_sensor"]["light"]
	
	def get_battery(self):
		payload = self.battery_sensor.read().decode('utf-8')
		payload_dit = ast.literal_eval(payload)
		return payload_dit["battery_sensor"]["battery"]