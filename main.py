import gpiozero as gz
import time
from datetime import datetime
import logging
import pygame as pg
import os

pg.mixer.init()

RELAY_2 = 22
RELAY_1 = 23

PIR_SENSOR = 24

def halloween():
	pir = gz.MotionSensor(PIR_SENSOR)
	relay1 = gz.OutputDevice(RELAY_1, active_high=False, initial_value=False)
	relay2 = gz.OutputDevice(RELAY_2, active_high=False, initial_value=False)

	logging.basicConfig(filename='halloween.log',level=logging.DEBUG)
	logging.debug('Starting Halloween')

	while True:
		try:
			now = datetime.now()
			pir.wait_for_motion(timeout = None)

			if pir.motion_detected:
				logging.info("Motion Detected - " + now.strftime("%d/%m/%Y %H:%M:%S"))

				relay1.on()
				logging.info('RELAY 1 on')
				pg.mixer.music.load("sounds/lightning.mp3")
				pg.mixer.music.play()
				time.sleep(5)
				relay1.off()

				relay2.on()
				logging.info('RELAY 2 on')
				pg.mixer.music.load("sounds/wolf_howl.mp3")
				pg.mixer.music.play()
				time.sleep(5)
				relay2.off()


			time.sleep(1)


		except Exception as e:
			logging.debug('Error: ' + str(e))


if __name__ == '__main__':
	halloween()
