import sensor
import image
import time
import utime
import utime
import pyb
import tf
import machine

from pyb import UART

uart = machine.UART(1, baudrate=9600)
uart = UART(1, 9600) # UART1, adjust baudrate as needed

redLED   = pyb.LED(1)

sensor.reset() # Initialize the camera sensor.
sensor.set_pixformat(sensor.RGB565) # or sensor.GRAYSCALE
sensor.set_framesize(sensor.QVGA)

sensor.skip_frames(time = 2000)


#red light during setup
redLED.on()


#Load the TFlite model and the labels, takes a lot of power.
net = tf.load('MNv2Flood_cat (3).tflite', load_to_fb=True)
labels = ['Flood', 'NoFlood']

#turn led off when model is loaded
redLED.off()

while(True):

    #check for sign of life.
    img = sensor.snapshot()

    TF_objs = net.classify(img)

    Flood = TF_objs[0].output()[0]
    NoFlood = TF_objs[0].output()[1]

    if Flood > NoFlood:
        print('Flood')
        uart.write('Flood')

    else:
        print('No Flood')
        uart.write('No Flood')
