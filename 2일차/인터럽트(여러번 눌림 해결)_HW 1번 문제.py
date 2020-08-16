# GPIO.IRQ_RISING를 이용해 while문을 써서 지속적으로 버튼이 눌렸는지
# 확인하지 않아도, 버튼의 값이 바뀔 때만 btn_function() 함수를 호출해서
# 버튼 출력 문구와 LED의 색상 상태가 바뀌도록 작성

from Maix import GPIO
import time

fm.register(8, fm.fpioa.GPIOHS0)
btn = GPIO(GPIO.GPIOHS0, GPIO.IN)

fm.register(9, fm.fpioa.GPIOHS1)
led = GPIO(GPIO.GPIOHS1, GPIO.OUT)

btn_time = 0
led_power = 0

def btn_function(pin_num):
    current_time = time.ticks()
    global btn_time
    global led_power
    # print(current_time - btn_time)
    if (current_time - btn_time) >= 500:
        print("버튼이 눌렸습니다.")
        led_power = not led_power
        led.value(led_power)
        btn_time = time.ticks()

btn.irq(btn_function, GPIO.IRQ_RISING)
