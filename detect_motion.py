from gpiozero import MotionSensor, LED
import time
from datetime import datetime

gpio_sensor = 24

pir = MotionSensor(gpio_sensor)

def on_motion():
	now = datetime.now()
	time_format = now.strftime("%Y-%m-%d %H:%M:%S")
	return time_format



while True:
	pir.wait_for_motion(timeout = None)
	print(on_motion())
	time.sleep(2)