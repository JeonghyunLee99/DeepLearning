# Maix 모듈(파이썬 파일)에서 GPIO라는 함수를 import 함
from Maix import GPIO
import time

# 핀을 레지스터 설정
fm.register(9, fm.fpioa.GPIOHS1)
led = GPIO(GPIO.GPIOHS1, GPIO.OUT)

while True:
    led.value(1)
    time.sleep(0.001)
    led.value(0)
    time.sleep(0.009)
