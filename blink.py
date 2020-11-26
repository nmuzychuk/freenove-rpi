import RPi.GPIO as GPIO
import time

ledPin = 11

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    print('using pin%d', ledPin)

def loop():
    while True:
        GPIO.output(ledPin, GPIO.HIGH)
        print('led turned on >>>')
        time.sleep(1)
        GPIO.output(ledPin, GPIO.LOW)
        print('led turned off <<<')
        time.sleep(1)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    print('Program is starting...\n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
