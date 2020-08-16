from Maix import GPIO
import time

fm.register(8, fm.fpioa.GPIOHS0)
btn = GPIO(GPIO.GPIOHS0, GPIO.IN)

fm.register(9, fm.fpioa.GPIOHS1)
led = GPIO(GPIO.GPIOHS1, GPIO.OUT)

while True:
    if btn.value() == 1 :
        print("LED on")
        led.value(1) # led.duty(100) 같은 의미
        time.sleep(0.5)
        if btn.value() == 1 :
            print("LED off")
            led.value(0)
            #led.duty(100)
            time.sleep(0.5)
