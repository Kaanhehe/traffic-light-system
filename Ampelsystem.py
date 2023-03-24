import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# Pin mappings
pins = {
    "ampel1_green": 25,
    "ampel1_yellow": 24,
    "ampel1_red": 23,
    "ampel2_green": 22,
    "ampel2_red": 21,
    "button": 10,
}
# Timing constants
ampel1_yellow_to_green_time = 3
ampel1_yellow_to_red_time = 3
ampel2_green_time = 10
puffer = 1
# Setup GPIO pins
for pin in pins.values():
    if "button" in pins and pins["button"] == pin:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    else:
        GPIO.setup(pin, GPIO.OUT)
# Function to control the traffic light
def control_traffic_light(ampel1_yellow_to_green_time, ampel1_yellow_to_red_time, ampel2_green_time, puffer):
    # Set initial states
    GPIO.output(pins["ampel1_green"], GPIO.HIGH)
    GPIO.output(pins["ampel2_red"], GPIO.HIGH)
    while True:
        try:
            # Check button state
            if GPIO.input(pins["button"]) == GPIO.HIGH:
                # Set traffic light to red for first intersection
                GPIO.output(pins["ampel1_green"], GPIO.LOW)
                GPIO.output(pins["ampel1_yellow"], GPIO.HIGH)
                time.sleep(ampel1_yellow_to_red_time)
                GPIO.output(pins["ampel1_yellow"], GPIO.LOW)
                GPIO.output(pins["ampel1_red"], GPIO.HIGH)
                time.sleep(puffer)
                # Set traffic light to green for second intersection
                GPIO.output(pins["ampel2_red"], GPIO.LOW)
                GPIO.output(pins["ampel2_green"], GPIO.HIGH)
                time.sleep(ampel2_green_time)
                GPIO.output(pins["ampel2_green"], GPIO.LOW)
                GPIO.output(pins["ampel2_red"], GPIO.HIGH)
                time.sleep(puffer)
                # Set traffic light to green for first intersection
                GPIO.output(pins["ampel1_yellow"], GPIO.HIGH)
                time.sleep(ampel1_yellow_to_green_time)
                GPIO.output(pins["ampel1_red"], GPIO.LOW)
                GPIO.output(pins["ampel1_yellow"], GPIO.LOW)
                GPIO.output(pins["ampel1_green"], GPIO.HIGH)
        except Exception as e:
            print(e)
            GPIO.cleanup()
            break
# Start controlling the traffic light
# Main
control_traffic_light(ampel1_yellow_to_green_time, ampel1_yellow_to_red_time, ampel2_green_time, puffer)
