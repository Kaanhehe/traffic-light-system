import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)


GPIO.setmode(GPIO.BCM)


# Questions
portgreen1 = 25
portyellow1 = 25
portred1 = 25
portgreen2 = 25
portred2 = 25
portbutton = 10
# Rot zu gelb
ampel1rtyt = 3
# gelb zu grün
ampel1ytgt = 2
# grün zu gelb
ampel1gtyt = 2
# Ampel gelb zu rot
ampel1ytrt = 3
# Fuß rot zu grün
ampel2rtgt = 2
# Fuß grün zu rot
ampel2gtrt = 10



#Ports bestimmen
GPIO.setup(portgreen1, GPIO.OUT)
GPIO.setup(portyellow1, GPIO.OUT)
GPIO.setup(portred1, GPIO.OUT)
GPIO.setup(portgreen2, GPIO.OUT)
GPIO.setup(portred2, GPIO.OUT)
GPIO.setup(portbutton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def ampeltored():
    GPIO.output(portgreen1, GPIO.LOW)
    GPIO.output(portyellow1, GPIO.HIGH)
    time.sleep(ampel1ytrt)
    GPIO.output(portyellow1, GPIO.LOW)
    GPIO.output(portred1, GPIO.HIGH)
    time.sleep(3)



GPIO.output(portgreen1, GPIO.HIGH)
GPIO.output(portred2, GPIO.HIGH)


if GPIO.input(portbutton) == GPIO.HIGH:
    ampeltored()
    GPIO.output(portred2, GPIO.LOW)
    GPIO.output(portgreen2, GPIO.HIGH)
    time.sleep(10)
    GPIO.output(portgreen2, GPIO.LOW)
    GPIO.output(portred2, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(portyellow1, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(portred1, GPIO.LOW)
    GPIO.output(portyellow1, GPIO.LOW)
    GPIO.output(portgreen1, GPIO.HIGH)