import RPi.GPIO as GPIO
from time import sleep
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

try:
    while True:
        GPIO.output(25, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(25,GPIO.LOW)
        sleep(0.5)

except KeyboardInterrupt:
    logging.info('Process aborted by user')

GPIO.cleanup()
