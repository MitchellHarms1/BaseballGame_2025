'''Main file the program will run on'''

import random
import time
from Questions import *

# def load_questions(filename="questions.txt"):
#     """Load questions and answers from a file into a list of tuples."""
#     questions = []
#     with open(filename, "r") as file:
#         for line in file:
#             if "|" in line:
#                 try: 
#                     (question, answer) = line.strip().split(" | ", 1)
#                 except: 
#                     pass
                
#                 questions.append((question, answer))
#     return questions

def get_random_Red_question():
    """Return a random question and answer tuple from the list of questions."""
    return random.choice(Red_questions)

def get_random_Blue_question():
    """Return a random question and answer tuple from the list of questions."""
    return random.choice(Blue_questions)

def get_random_Green_question():
    """Return a random question and answer tuple from the list of questions."""
    return random.choice(Green_questions)

def get_random_Yellow_question():
    """Return a random question and answer tuple from the list of questions."""
    return random.choice(Yellow_questions)
# Load questions from file
# questions = load_questions()

# # Get a random question and answer
# question, answer = get_random_question(questions)
# print("Question:", question)

# # Wait for 10 seconds before showing the answer
# time.sleep(10)
# print("Answer:", answer)

def get_structured_question(question):
    questionsplit = question.split('|')
    return {
        "question": questionsplit[0],
        "answer" : questionsplit[1],
    }

# def turn(color): 
#     question = get_random_question(questions[color])
#     StructuredQuestion = get_structured_question(question)
#     print(StructuredQuestion['question'])
#     time.sleep(10)
#     print(StructuredQuestion['answer'])


def turn (color):
    if color == 'red':
       structuredquestion = get_structured_question(get_random_Red_question())
    if color == 'blue':
       structuredquestion = get_structured_question(get_random_Blue_question())
    if color == 'green':
       structuredquestion = get_structured_question(get_random_Green_question())
    if color == 'yellow':
       structuredquestion = get_structured_question(get_random_Yellow_question())
    print(structuredquestion['question'])
    time.sleep(10)
    print(structuredquestion['answer'])

for i in range(1):
    user = input('Color Input: \n')
    turn(user)
    time.sleep(1)

'''
Code for adding the button tor the above 

import RPi.GPIO as GPIO
import random
import time

# Define GPIO pins for each button
BUTTON_PIN_1 = 5  # GPIO pin connected to button 1
BUTTON_PIN_2 = 26  # GPIO pin connected to button 2
BUTTON_PIN_3 = 13  # GPIO pin connected to button 3
BUTTON_PIN_4 = 6  # GPIO pin connected to button 4

# Set up GPIO mode and pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN_4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Function to load questions from a file into a list of tuples
def load_questions(filename):
    """Load questions and answers from a file into a list of tuples."""
    questions = []
    try:
        with open(filename, "r") as file:
            for line in file:
                if "|" in line:
                    question, answer = line.strip().split(" | ", 1)
                    questions.append((question, answer))
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return questions

# Function to get a random question from a list of questions
def get_random_question(questions):
    """Return a random question and answer tuple from the list of questions."""
    if questions:
        return random.choice(questions)
    else:
        return None, None

# Load question sets from files
question_files = {
    BUTTON_PIN_1: "questions1.txt",
    BUTTON_PIN_2: "questions2.txt",
    BUTTON_PIN_3: "questions3.txt"
    BUTTON_PIN_4: "questions4.txt"
}
question_sets = {pin: load_questions(filename) for pin, filename in question_files.items()}

# Function to handle button press
def button_callback(channel):
    print(f"Button on GPIO {channel} Pressed")
    questions = question_sets.get(channel)
    if questions:
        question, answer = get_random_question(questions)
        if question:
            print("Question:", question)
            time.sleep(10)  # Wait for 10 seconds before showing the answer
            print("Answer:", answer)
        else:
            print("No questions available for this set.")
    else:
        print("No questions loaded for this button.")

# Set up event detection for each button
GPIO.add_event_detect(BUTTON_PIN_1, GPIO.FALLING, callback=button_callback, bouncetime=300)
GPIO.add_event_detect(BUTTON_PIN_2, GPIO.FALLING, callback=button_callback, bouncetime=300)
GPIO.add_event_detect(BUTTON_PIN_3, GPIO.FALLING, callback=button_callback, bouncetime=300)
GPIO.add_event_detect(BUTTON_PIN_4, GPIO.FALLING, callback=button_callback, bouncetime=300)


# Main loop
try:
    print("Press a button to get a random question from the corresponding set.")
    while True:
        # Keep the script running to detect button presses
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting program.")

finally:
    # Clean up GPIO settings
    GPIO.cleanup()
'''