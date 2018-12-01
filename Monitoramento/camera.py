from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180

camera.start_preview()
camera.start_recording('/home/pi/Monitoramento/video.h264')
camera.wait_recording(10)
camera.stop_recording()
camera.stop_preview()