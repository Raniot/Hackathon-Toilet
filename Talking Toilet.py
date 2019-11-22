#Libraries

import RPi.GPIO as GPIO
import os
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins

GPIO_TRIGGER = 18
GPIO_ECHO = 24

GPIO_TRIGGER2 = 17
GPIO_ECHO2 = 22


#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)

def distance(trigger, echo):

    # set Trigger to HIGH
    print('trigger: %d' % trigger)
    print('echo: %d' % echo)
    GPIO.output(trigger, True)

    # set Trigger after 0.01ms to LOW

    time.sleep(0.00001)

    GPIO.output(trigger, False)

    StartTime = time.time()

    StopTime = time.time()

    # save StartTime

    while GPIO.input(echo) == 0:

        StartTime = time.time()

    # save time of arrival

    while GPIO.input(echo) == 1:

        StopTime = time.time()

    # time difference between start and arrival

    TimeElapsed = StopTime - StartTime

    # multiply with the sonic speed (34300 cm/s)

    # and divide by 2, because there and back

    distance = (TimeElapsed * 34300) / 2

    return distance

if __name__ == '__main__':

    try:

        isOnTheCan = False
        poopCounter = 1

        while True:
            dist1 = distance(GPIO_TRIGGER, GPIO_ECHO2)
            print ("Measured Distance = %.1f cm" % dist1)

            if(dist1 < 20 and isOnTheCan and poopCounter == 1):
                os.system("aplay /home/pi/quakesounds/firstblood.wav")
                poopCounter = poopCounter + 1

            elif(dist1 < 20 and isOnTheCan and poopCounter == 2):
                os.system("aplay /home/pi/quakesounds/doublekill.wav")
                poopCounter = poopCounter + 1

            elif(dist1 < 20 and isOnTheCan and poopCounter == 3):
                os.system("aplay /home/pi/quakesounds/triplekill.wav")
                poopCounter = poopCounter + 1

            elif(dist1 < 20 and isOnTheCan and poopCounter == 4):
                os.system("aplay /home/pi/quakesounds/killingspree.wav")
                poopCounter = poopCounter + 1
            
            elif(dist1 < 20 and isOnTheCan and poopCounter == 5):
                os.system("aplay /home/pi/quakesounds/godlike.wav")
                poopCounter = poopCounter + 1

            dist2 = distance(GPIO_TRIGGER, GPIO_ECHO)
            print ("Measured Distance2 = %.1f cm" % dist2)
	    
            if(dist2 < 20 and not isOnTheCan):
                os.system("aplay /home/pi/quakesounds/prepare.wav")
                isOnTheCan = True

            if(dist2 > 70 and isOnTheCan):
                if(poopCounter <= 4):
                    os.system("aplay /home/pi/quakesounds/humiliation.wav")
                else:
                    os.system("aplay /home/pi/quakesounds/perfect.wav")
                poopCounter = 1
                isOnTheCan = False

            #time.sleep(0.05)


        # Reset by pressing CTRL + C

    except KeyboardInterrupt:

        print("Measurement stopped by User")

        GPIO.cleanup()
