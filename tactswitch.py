import logging
import RPi.GPIO as GPIO
from time import sleep

logger = logging.getLogger()
logger.setLevel(logging.INFO)


GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.IN)
# raspi内部のプルダウン抵抗を使いたいとき
#GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(24) == GPIO.HIGH:
            GPIO.output(25, GPIO.HIGH)
        else:
            GPIO.output(25, GPIO.LOW)

        sleep(0.01)

except KeyboardInterrupt:
    logging.info('process aborted by user')

GPIO.cleanup()
