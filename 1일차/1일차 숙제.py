from Maix import GPIO
import time

fm.register(8, fm.fpioa.GPIOHS0)
btn = GPIO(GPIO.GPIOHS0, GPIO.IN)

fm.register(9, fm.fpioa.GPIOHS1)
led = GPIO(GPIO.GPIOHS1, GPIO.OUT)

while True:
    if btn.value() == 1:
        led.value(1)
    else:
        led.value(0)

    # time.sleep(0.1)
