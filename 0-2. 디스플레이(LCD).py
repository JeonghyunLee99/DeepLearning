```python
import sensor, image, lcd, time

lcd.init()

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((320, 240))
sensor.run(1)
sensor.set_vflip(0)
sensor.set_hmirror(0)
clock = time.clock()

while True:
    clock.tick()
    img = sensor.snapshot()
    fps=clock.fps()
    lcd.display(img)
    print(fps)
```