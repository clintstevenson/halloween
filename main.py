import gpiozero as gz
import time
from datetime import datetime
import logging
import pygame as pg
import os

# Set GPIO pins
RELAY_2 = 22
RELAY_1 = 23
PIR_SENSOR = 24

# Halloween function
def halloween():
    # Initialized the sensor, relay 1, and relay 2
    pir = gz.MotionSensor(PIR_SENSOR)
    relay1 = gz.OutputDevice(RELAY_1, active_high=False, initial_value=False)
    relay2 = gz.OutputDevice(RELAY_2, active_high=False, initial_value=False)

    logging.basicConfig(filename='halloween.log',level=logging.DEBUG)
    logging.debug('Starting Halloween')

    pg.mixer.init()
    
    try:
        while True:
            # Keep attempting to execute the program even after error is thrown.
            if not pir:
                raise Exception("PIR sensor not detected")

            try:
                now = datetime.now()
                # Sit and wait this command until motion is detected
                pir.wait_for_motion(timeout = None)

                # If motion is detected then turn the relay on and play the sounds.
                if pir.motion_detected:
                    logging.info("Motion Detected - " + now.strftime("%d/%m/%Y %H:%M:%S"))

                    relay1.on()
                    logging.info('RELAY 1 on')
                    pg.mixer.music.load("sounds/lightning.mp3")
                    pg.mixer.music.play()
                    time.sleep(7)
                    relay1.off()

                    relay2.on()
                    logging.info('RELAY 2 on')
                    pg.mixer.music.load("sounds/wolf_howl.mp3")
                    pg.mixer.music.play()
                    time.sleep(7)
                    relay2.off()

                time.sleep(1)

            except Exception as e:
                logging.debug('Error: ' + str(e))
    except KeyboardInterrupt:
            pir.close()
            relay1.close()
            relay2.close()


if __name__ == '__main__':    
    halloween()
