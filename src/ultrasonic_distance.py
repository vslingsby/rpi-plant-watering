# code modified from source: https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/

#Libraries
import RPi.GPIO as GPIO
import time

class UltrasonicDistance:
    #set GPIO Pins
    GPIO_TRIGGER = 18
    GPIO_ECHO = 24

    def __init__(self,trigger,echo):
        self.GPIO_TRIGGER = trigger
        self.GPIO_ECHO = echo

    def __del__(self):
        GPIO.cleanup()

    def distance(self):
        #GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)

        #set GPIO direction (IN / OUT)
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)

        # set Trigger to HIGH
        GPIO.output(self.GPIO_TRIGGER, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while GPIO.input(self.GPIO_ECHO) == 0:
            StartTime = time.time()

        # save time of arrival
        while GPIO.input(self.GPIO_ECHO) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        GPIO.cleanup()
        return distance
