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
# ampel grün wie lange gelb
ampel1ytgt = 3
# Ampel rot wie lange gelb
ampel1ytrt = 3
# Fuß wie lange grün
ampel2gtrt = 10
# Puffer
puffer = 1


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
    time.sleep(puffer)
def ampeltogreen():
    GPIO.output(portred1, GPIO.LOW)
    GPIO.output(portyellow1, GPIO.HIGH)
    time.sleep(ampel1ytgt)
    GPIO.output(portyellow1, GPIO.LOW)
    GPIO.output(portgreen1, GPIO.HIGH)
    time.sleep(puffer)
def ampeltogreen2():
    GPIO.output(portred2, GPIO.LOW)
    GPIO.output(portgreen2, GPIO.HIGH)
    time.sleep(ampel2gtrt)
    GPIO.output(portgreen2, GPIO.LOW)
    GPIO.output(portred2, GPIO.HIGH)
    time.sleep(puffer)


GPIO.output(portgreen1, GPIO.HIGH)
GPIO.output(portred2, GPIO.HIGH)

if GPIO.input(portbutton) == GPIO.HIGH:
    ampeltored()
    ampeltogreen2()
    ampeltogreen()
