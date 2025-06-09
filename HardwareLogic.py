'''Button input and scrolling text'''

import RPi.GPIO as GPIO
from Main import turn

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
button_pins = [5, 26, 13, 6]  # GpPIO pins for buttons
question_list = ["question_set1", "Question 2", "Question 3", "Question 4"]  # List of questions

for pin in button_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        for i, pin in enumerate(button_pins):
            if GPIO.input(pin) == GPIO.LOW:
                turn()

except KeyboardInterrupt:
    GPIO.cleanup()