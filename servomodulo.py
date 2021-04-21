import RPi.GPIO as GPIO
import time
P_SERVO = 26
fPWM = 50 
a = 10
b = 2
GPIO.setmode(GPIO.BOARD)
GPIO.setup(P_SERVO, GPIO.OUT)
pwm = GPIO.PWM(P_SERVO, fPWM)

def setDirection(direction):
    pwm.start(0)
    duty = a / 180 * direction + b
    pwm.ChangeDutyCycle(duty)
    print ("direction =", direction, "-> duty =", duty)
    time.sleep(0.4) # allow to settle
    pwm.ChangeDutyCycle(0)
    time.sleep(0.1)
    return duty