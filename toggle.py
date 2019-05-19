import logging
import RPi.GPIO as GPIO
from time import sleep

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ledState = GPIO.LOW

def my_callback(channel):
    global ledState
    if channel==24:
        ledState = not ledState
        GPIO.output(25, ledState)

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(24, GPIO.RISING, callback=my_callback, bouncetime=200)

def main():
    try:
        while True:
            sleep(0.01)
    except KeyboardInterrupt:
        logging.info('process aborted by user')
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
