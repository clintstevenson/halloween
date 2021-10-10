from gpiozero import MotionSensor, LED
import time
from datetime import datetime
import logging

PIR_SENSOR = MotionSensor(17)
relay1 = LED(27)
relay2 = LED(22)

def halloween():
	logging.basicConfig(filename='halloween.log',level=logging.DEBUG)
	logging.debug('Starting Halloween')

	while True:
		try:
			# PIR_SENSOR.wait_for_motion()
			now = datetime.now()
			logging.info("Motion Detected - " + now.strftime("%d/%m/%Y %H:%M:%S"))

			logging.info('Relay1 on')
			PIR_SENSOR.when_motion = relay1.on
			time.sleep(1)
			logging.info('Relay2 on')
			PIR_SENSOR.when_motion = relay2.on

			# PIR_SENSOR.when_no_motion = relay1.off
			# PIR_SENSOR.when_no_motion = relay2.off

			time.sleep(5)
			relay1.off
			relay2.off
			time.sleep(5)
			# PIR_SENSOR.when_motion = relay.on
			# time.sleep(1)

			# PIR_SENSOR.when_no_motion = relay.off
			# logging.info('Relay off')
			time.sleep(5)
		except Exception as e:
			logging.debug('Error: ' + str(e))


# GPIO.output(3, 0)
# time.sleep(1)

if __name__ == '__main__':
	halloween()
