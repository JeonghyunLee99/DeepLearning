import sensor, image, lcd, time
import KPU as kpu
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((224, 224))
sensor.set_vflip(0)
sensor.set_hmirror(1)
sensor.run(1)
lcd.clear()


task = kpu.load(0x300000) 
clock = time.clock()

while(True):
    img = sensor.snapshot()
    clock.tick()
    fmap = kpu.forward(task, img)
    plist=fmap[:]
    print(plist)
    lcd.display(img)
a = kpu.deinit(task)