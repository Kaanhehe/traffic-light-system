import RPi.GPIO as GPIO
import time
import argparse
import logging


# Configure logging
logging.basicConfig(level=logging.INFO)


# Pin mappings
PINS = {
    "ampel1_green": 25,
    "ampel1_yellow": 24,
    "ampel1_red": 23,
    "ampel2_green": 22,
    "ampel2_red": 21,
    "button": 10,
}


# Setup GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


for pin in PINS.values():
    if pin == PINS["button"]:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    else:
        GPIO.setup(pin, GPIO.OUT)



def control_traffic_light(yellow_to_green_duration, yellow_to_red_duration, green_duration, puffer):
    """Let the pedestrian cross the street and the cars wait.
    Args:
        yellow_to_green_duration (int): Duration of the yellow light before the green light turns on.
        yellow_to_red_duration (int): Duration of the yellow light before the red light turns on.
        green_duration (int): Duration of the green light for the pedestrian.
        puffer (int): Duration of the buffer time between traffic light changes.
    """
    
    # Set initial states
    GPIO.output(PINS["ampel1_green"], GPIO.HIGH)
    GPIO.output(PINS["ampel2_red"], GPIO.HIGH)
    
    
    while True:
        try:
            # Check button state
            if GPIO.input(PINS["button"]) == GPIO.HIGH:
                # Set traffic light to red for first intersection
                GPIO.output(PINS["ampel1_green"], GPIO.LOW)
                GPIO.output(PINS["ampel1_yellow"], GPIO.HIGH)
                time.sleep(yellow_to_red_duration)
                GPIO.output(PINS["ampel1_yellow"], GPIO.LOW)
                GPIO.output(PINS["ampel1_red"], GPIO.HIGH)
                time.sleep(puffer)
                # Set traffic light to green for second intersection
                GPIO.output(PINS["ampel2_red"], GPIO.LOW)
                GPIO.output(PINS["ampel2_green"], GPIO.HIGH)
                time.sleep(green_duration)
                GPIO.output(PINS["ampel2_green"], GPIO.LOW)
                GPIO.output(PINS["ampel2_red"], GPIO.HIGH)
                time.sleep(puffer)
                # Set traffic light to green for first intersection
                GPIO.output(PINS["ampel1_yellow"], GPIO.HIGH)
                time.sleep(yellow_to_green_duration)
                GPIO.output(PINS["ampel1_red"], GPIO.LOW)
                GPIO.output(PINS["ampel1_yellow"], GPIO.LOW)
                GPIO.output(PINS["ampel1_green"], GPIO.HIGH)
        
        except Exception as e:
            logging.exception(e)
            break

    GPIO.cleanup()
    logging.info("Cleaned up GPIO resources.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Let the pedestrian cross the street and the cars wait.")
    parser.add_argument("yellow_to_green_duration", type=int, help="Duration of the yellow light before the green light turns on.")
    parser.add_argument("yellow_to_red_duration", type=int, help="Duration of the yellow light before the red light turns on.")
    parser.add_argument("green_duration", type=int, help="Duration of the green light.")
    parser.add_argument("puffer", type=int, help="Duration of the buffer time between traffic light changes.")
    args = parser.parse_args()
    control_traffic_light(args.yellow_to_green_duration, args.yellow_to_red_duration, args.green_duration, args.puffer)


# python Ampelsystem.py 3 3 10 1