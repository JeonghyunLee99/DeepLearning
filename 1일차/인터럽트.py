from Maix import GPIO
import time

def btn_function(pin_num):
    print("버튼이 눌렸습니다.")

fm.register(8, fm.fpioa.GPIOHS0)
btn = GPIO(GPIO.GPIOHS0, GPIO.IN)

btn.irq(btn_function, GPIO.IRQ_RISING)
