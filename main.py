import RPi.GPIO as GPIO
import time
import dht11-raspberrypi/dht11

servoPIN = 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

# read data using Pin GPIO21 
instance = dht11.DHT11(pin=21)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

while True:
    result = instance.read()
    if result.is_valid():
        print("Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity)

    if result.temperature == 0:
        continue

    if result.temperature <= 15:
        p.ChangeDutyCycle(5)
        print("low")

    elif result.temperature > 15 and result.temperature <= 25:
        p.ChangeDutyCycle(7.5)
        print("mid")

    elif result.temperature > 25 and result.temperature:
        p.ChangeDutyCycle(12.5)
        print("high")

    time.sleep(0)