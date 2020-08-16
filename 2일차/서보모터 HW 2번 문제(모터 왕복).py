from machine import Timer,PWM
import time

# there are 3 timers and each timer has 4 channels
tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PWM)
S1 = PWM(tim, freq=50, duty=0, pin=12)
tim2 = Timer(Timer.TIMER0, Timer.CHANNEL1, mode=Timer.MODE_PWM)
S2 = PWM(tim2, freq=50, duty=0, pin=13)

# 4.25 < a < 13 / 5.25 < b < 9.25
def servoPosition(a, b):
    if a < 4.25:
        a = 4.25
    if a > 13:
        a = 13
    if b < 5.25:
        b = 5.25
    if b > 9.25:
        b = 9.25

    S1.duty(a)
    S2.duty(b)

while True:
    i = 4.25
    while i <= 13:
        #print(i)
        servoPosition(i, 7.5)
        time.sleep(0.01)
        i = i + 0.01
    while i >= 4.25:
        #print(i)
        servoPosition(i, 7.5)
        time.sleep(0.01)
        i = i - 0.01
