from Maix import GPIO
import time

fm.register(9, fm.fpioa.GPIOHS1)
led = GPIO(GPIO.GPIOHS1, GPIO.OUT)

fm.register(8, fm.fpioa.GPIOHS0)
btn = GPIO(GPIO.GPIOHS0, GPIO.IN)

# 핵심: LED의 상태를 반드시 변수에 저장해야 함
# LED가 켜져 있으면(1) => 끄고(0)
# LED가 꺼져 있으면(0) => 켜야 함(1)

led_state = 0

while True:
    if btn.value() == 1 :
        led_state = not led_state
        led.value(led_state)
        time.sleep(0.5)
