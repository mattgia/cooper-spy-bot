import RPi.GPIO as GPIO
import signal
import os

MOTOR_LEFT_FORWARD_ID = int(os.environ['MOTOR_LEFT_FORWARD_ID'])
MOTOR_RIGHT_FORWARD_ID = int(os.environ['MOTOR_RIGHT_FORWARD_ID'])
MOTOR_LEFT_BACKWARD_ID = int(os.environ['MOTOR_LEFT_BACKWARD_ID'])
MOTOR_RIGHT_BACKWARD_ID = int(os.environ['MOTOR_RIGHT_BACKWARD_ID'])

MOTOR_LEFT_TRIM = int(os.environ['MOTOR_LEFT_TRIM'])
MOTOR_RIGHT_TRIM = int(os.environ['MOTOR_RIGHT_TRIM'])

GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_LEFT_FORWARD_ID, GPIO.OUT)
GPIO.setup(MOTOR_RIGHT_FORWARD_ID, GPIO.OUT)
GPIO.setup(MOTOR_LEFT_BACKWARD_ID, GPIO.OUT)
GPIO.setup(MOTOR_RIGHT_BACKWARD_ID, GPIO.OUT)

left = GPIO.PWM(MOTOR_LEFT_FORWARD_ID, 1000)
right = GPIO.PWM(MOTOR_RIGHT_FORWARD_ID, 1000)
left_reverse = GPIO.PWM(MOTOR_LEFT_BACKWARD_ID, 1000)
right_reverse = GPIO.PWM(MOTOR_RIGHT_BACKWARD_ID, 1000)

def gpio_reset(*args):
    GPIO.cleanup()
    print('cleaned up GPIO')

signal.signal(signal.SIGTERM, gpio_reset)
signal.signal(signal.SIGINT, gpio_reset)


def forward(speed = 100):
    _reset()
    left.start(speed * MOTOR_LEFT_TRIM)
    right.start(speed * MOTOR_RIGHT_TRIM)

def backward(speed = 100):
    _reset()
    left_reverse.start(speed * MOTOR_LEFT_TRIM)
    right_reverse.start(speed * MOTOR_RIGHT_TRIM)

def turn_left(speed = 100):
    _reset()
    left_reverse.start(speed * MOTOR_LEFT_TRIM)
    right.start(speed * MOTOR_RIGHT_TRIM)
    

def turn_right(speed = 100):
    _reset()
    left.start(speed * MOTOR_LEFT_TRIM)
    right_reverse.start(speed * MOTOR_RIGHT_TRIM)

def _reset():
    left.stop()
    right.stop()
    left_reverse.stop()
    right_reverse.stop()
