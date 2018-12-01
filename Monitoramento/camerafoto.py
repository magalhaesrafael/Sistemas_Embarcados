from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180

camera.start_preview()
for i in range(3):
    sleep(2)
    camera.capture('/home/pi/Monitoramento/imagem%s.jpg' % i)
camera.stop_preview()