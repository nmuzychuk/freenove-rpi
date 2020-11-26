import RPi.GPIO as GPIO

ledPin = 11  # define ledPin
buttonPin = 12  # define buttonPin def setup():


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def loop():
    while True:
        # set buttonPin to PULL UP
        if GPIO.input(buttonPin) == GPIO.LOW:  # if button is pressed
            GPIO.output(ledPin, GPIO.HIGH)  # turn on led
            print('led turned on >>>')  # print information on terminal
        else:  # if button is released
            GPIO.output(ledPin, GPIO.LOW)  # turn off led
            print('led turned off <<<')


def destroy():
    GPIO.cleanup()  # Release GPIO resource


if __name__ == '__main__':  # Program entrance
    print('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
