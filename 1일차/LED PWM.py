from machine import Timer,PWM
import time

tim3 = Timer(Timer.TIMER0, Timer.CHANNEL2, mode=Timer.MODE_PWM)
led = PWM(tim3, freq=5000, duty=0, pin=9)
# freq: 주파수 프레임을 높일수록 1/5000 초에 1번씩 깜빡임
1 / 5: 5초에 1번씩 깜빡이는 건 눈에 잘 띄임

while True:
    for i in range(100):
        led.duty(i)
        time.sleep(0.01)
    for i in range(100, -1, -1):
        led.duty(i)
        time.sleep(0.01)

# 서보 보터는 기본적으로 50Hz 단위로 움직임(제작 회사 기준)
