from anif.mqttif import MQTTSubscribeInterface


class VirtualSensor():
	def __init__(self, addr, port):
		self._interface = MQTTSubscribeInterface(addr, port)
	
	def enable(self, file):
		self._interface.open(file)
	
	def disable(self):
		self._interface.close()

	def read(self):
		return self._interface.read()
	

class VirtualAccelerometerSensor(VirtualSensor):
	pass


class VirtualHumiditySensor(VirtualSensor):
	pass


class VirtualMagnetometerSensor(VirtualSensor):
	pass


class VirtualBarometerSensor(VirtualSensor):
	pass


class VirtualGyroscopeSensor(VirtualSensor):
	pass


class VirtualLightSensor(VirtualSensor):
	pass


class VirtualBatterySensor(VirtualSensor):
	pass

