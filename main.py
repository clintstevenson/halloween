from gpiozero import MotionSensor, LED
import time
from datetime import datetime
import logging

logging.basicConfig(filename='halloween.log',level=logging.DEBUG)
logging.debug('Starting Halloween')

PIR_SENSOR = MotionSensor(17)
relay = LED(27)

while True:
	try:
		PIR_SENSOR.wait_for_motion()
		now = datetime.now()
		logging.info("Motion Detected - " + now.strftime("%d/%m/%Y %H:%M:%S"))



		logging.info('Relay on')
		PIR_SENSOR.when_motion = relay.on
		time.sleep(5)

		logging.info('Relay off')
		PIR_SENSOR.when_no_motion = relay.off
		time.sleep(10)
	except Exception as e:
		logging.debug('Error: ' + str(e))


# GPIO.output(3, 0)
# time.sleep(1)

