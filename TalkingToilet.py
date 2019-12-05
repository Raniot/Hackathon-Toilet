#Libraries

import RPi.GPIO as GPIO
import os
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins

GPIO_TRIGGER = 18
GPIO_ECHO = 22

GPIO_TRIGGER2 = 17
GPIO_ECHO2 = 24


#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)

def distance(trigger, echo):

    # set Trigger to HIGH
    GPIO.output(trigger, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)

    # set Trigger to LOW
    GPIO.output(trigger, False)

    StartTime = time.time()
    StopTime = time.time()
    
    # save StartTime
    while GPIO.input(echo) == 0:
        StartTime = time.time()
        if StartTime - StopTime > 0.1:
            return -1
        

    # save time of arrival
    while GPIO.input(echo) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime

    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    if distance < 3:
        return -1

    return distance

if __name__ == '__main__':

    try:

        #Debugging - write out the distance every second.
        # while True:
        #     distToPoop = distance(GPIO_TRIGGER, GPIO_ECHO2)
        #     distToPerson = distance(GPIO_TRIGGER, GPIO_ECHO)

        #     if distToPoop == -1 or distToPerson == -1:
        #         continue

        #     print ("Measured Distance = %.1f cm" % distToPoop)
        #     print ("Measured Distance2 = %.1f cm" % distToPerson)

        #     time.sleep(1)

        isOnTheCan = False
        isNotOnTheCanCounter = 0
        poopCounter = 1

        while True:
            
            #Distance to object in toilet
            distToPoop = distance(GPIO_TRIGGER, GPIO_ECHO2)
            if distToPoop == -1:
                continue
            
            print ("Measured Distance to poop = %.1f cm" % distToPoop)

            if(distToPoop < 20 and isOnTheCan and poopCounter == 1):
                os.system("aplay /home/pi/quakesounds/firstblood.wav")
                poopCounter = poopCounter + 1

            elif(distToPoop < 20 and isOnTheCan and poopCounter == 2):
                os.system("aplay /home/pi/quakesounds/doublekill.wav")
                poopCounter = poopCounter + 1

            elif(distToPoop < 20 and isOnTheCan and poopCounter == 3):
                os.system("aplay /home/pi/quakesounds/triplekill.wav")
                poopCounter = poopCounter + 1

            elif(distToPoop < 20 and isOnTheCan and poopCounter == 4):
                os.system("aplay /home/pi/quakesounds/killingspree.wav")
                poopCounter = poopCounter + 1
            
            elif(distToPoop < 20 and isOnTheCan and poopCounter == 5):
                os.system("aplay /home/pi/quakesounds/godlike.wav")
                poopCounter = poopCounter + 1

            elif(distToPoop < 20 and isOnTheCan and poopCounter == 6):
                os.system("aplay /home/pi/quakesounds/monsterkill.wav")
                poopCounter = poopCounter + 1

            elif(distToPoop < 20 and isOnTheCan and poopCounter == 7):
                os.system("aplay /home/pi/quakesounds/holyshit.wav")
                poopCounter = poopCounter + 1

            #Distance to ass
            distToPerson = distance(GPIO_TRIGGER, GPIO_ECHO)
            if distToPerson == -1:
                continue

            print ("Measured Distance to person = %.1f cm" % distToPerson)
	    
            if(distToPerson < 20 and not isOnTheCan):
                os.system("aplay /home/pi/quakesounds/prepare.wav")
                isOnTheCan = True

            if(distToPerson < 20 and isOnTheCan):
                isNotOnTheCanCounter = 0

            if(distToPerson > 70 and isOnTheCan):
                if isNotOnTheCanCounter > 3:
                    isNotOnTheCanCounter = 0
                    poopCounter = 1
                    isOnTheCan = False
                    os.system("aplay /home/pi/quakesounds/perfect.wav")
                else:
                    isNotOnTheCanCounter = isNotOnTheCanCounter + 1
                
                # if(poopCounter <= 4):
                #     os.system("aplay /home/pi/quakesounds/humiliation.wav")
                # else:
                    # os.system("aplay /home/pi/quakesounds/perfect.wav")
                

            time.sleep(0.05)


        # Reset by pressing CTRL + C
    except KeyboardInterrupt:

        print("Measurement stopped by User")

        GPIO.cleanup()
