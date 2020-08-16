from Maix import GPIO
import time

fm.register(9, fm.fpioa.GPIOHS1)
led = GPIO(GPIO.GPIOHS1, GPIO.OUT)

while True:
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)
