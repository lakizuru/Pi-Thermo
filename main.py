# Importing  libraries
import RPi.GPIO as GPIO
import time
import dht11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

# read data using Pin GPIO21 
instance = dht11.DHT11(pin=21)

servoPIN = 17 # Servo motor is connected to GPIO 17
servo = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz

servo.start(2.5) # Initialization servo motor to 2.5% duty cycle

# Starting never ending loop
while True:
    result = instance.read() # Reading sensor input
    if result.is_valid():
        print("Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity)

    # Ignore if temperature is 0 as it is not practically valid
    if result.temperature == 0:
        continue

    # Duty Cycle is calculated as follows
    # 0 degrees angle = 2.5% duty cycle
    # 90 degrees angle = 7.5% duty cycle
    # 180 degrees angle = 12.5% duty cycle

    if result.temperature <= 15:
        servo.ChangeDutyCycle(5)
        print("low")

    elif result.temperature > 15 and result.temperature <= 25:
        servo.ChangeDutyCycle(7.5)
        print("mid")

    elif result.temperature > 25 and result.temperature:
        servo.ChangeDutyCycle(12.5)
        print("high")

    time.sleep(0)