##################### INTRODUCTION

##### OS installation
#ctrl + alt + t
$ sudo apt-get update
$ sudo apt-get upgrade
#If ERROR,solution:
$ sudo nano /etc/apt/sources.list
#Replace everything here with:
deb http://archive.raspbian.org/raspbian jessie main contrib non-free
deb-src http://archive.raspbian.org/raspbian jessie main contrib non-free
#control+x, y, enter
$ sudo apt-get dist-upgrade
$ sudo apt-get update
$ sudo apt-get upgrade
#To save some space: 
$ sudo apt-get purge wolfram-engine and then $ sudo apt-get autoremove. 

##### Remote access with RPi
sudo apt-get remove xrdp vnc4server tightvncserver
sudo apt-get install tightvncserver
sudo apt-get install xrdp


##### Terminal navigation
$ pwd #(print working directory): usually '/home/pi.'
$ sudo #super user is sudo, which is short for "super user do." administrator permissions
$ cd #"change directory." : To move around the system
$ ls #to discover the contents of the directory you are in
$ mkdir example #to make own directory names example in the working directory
$ ls
$ cd example #chaneg the directory to example
$ cd # to move backward to last directory
$ cd example
$ nano test.py #create a simple file with any of the built in editors.
#add: print("hi") to this file. When done, we can exit with control+x, then press y to save, and then enter to keep the name.
#To run this file, we can do: 
$ python test.py
#make another directory:
$ mkdir downloads
$ cd downloads
wget https://<link>/image.png # to get the image downloaded in pwd
$ ls
$ sudo apt-get install git # install git. 
$~/example/downloads $ git clone https://github.com/xxxxx # to clone github repositories.
$ ls
$ mkdir delme
$ ls
$ rmdir delme
$ ls
$ rmdir downloads/ # failed to remove
$ cd ~
$ ls
$ ls -al
$ ls --help
$ sudo shutdown -h now # Shutdown
$ sudo shutdown -r now or sudo reboot # Restart

##### RPi Camera module
#ctrl + alr + t
$ sudo raspi-config
# interfacing options > P1 Camera (enable (YES) and reboot) > Createa new empty file on desktop(cameraexample.py)
# ctrl + alt + t
$ sudo apt-get install python3-picamera
import picamera
import time
camera=picamera.Picamera() #define the camera object as camera
camera.capture('image.jpg') # .capture() to snap a quick photo
camera.vflip=True #flip the camera vertically  or horizontally if the image is flipped using .vflip or .hflip
camera.capture('image2.jpg') 
camera.start_recording('imagevideo.h264') #start recordning
time.sleep(5)
camera.stop_recording()	# stop recording

##### GPIO (General Purpose Input Output) Pins
$ sudo apt-get install python-rpi.gpio 

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.HIGH)

time.sleep(3)

GPIO.output(18, GPIO.LOW)
GPIO.cleanup()

##### Input from a Sensor via GPIO

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 18

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO) == False:
    start = time.time()

while GPIO.input(ECHO) == True:
    end = time.time()

sig_time = end-start

#CM:
distance = sig_time / 0.000058

#inches:
#distance = sig_time / 0.000148

print('Distance: {} centimeters'.format(distance))

GPIO.cleanup()

##### Garage Stoplight GPIO
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
# doing this first, since we're using a while True.
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
TRIG = 4
ECHO = 18

GREEN = 17
YELLOW = 27
RED = 22

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(YELLOW,GPIO.OUT)
GPIO.setup(RED,GPIO.OUT)


def green_light():
    GPIO.output(GREEN, GPIO.HIGH)
    GPIO.output(YELLOW, GPIO.LOW)
    GPIO.output(RED, GPIO.LOW)

def yellow_light():
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(YELLOW, GPIO.HIGH)
    GPIO.output(RED, GPIO.LOW)

def red_light():
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(YELLOW, GPIO.LOW)
    GPIO.output(RED, GPIO.HIGH)


def get_distance():


    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == False:
        start = time.time()

    while GPIO.input(ECHO) == True:
        end = time.time()

    sig_time = end-start

    #CM:
    distance = sig_time / 0.000058

    #inches:
    #distance = sig_time / 0.000148
    #print('Distance: {} centimeters'.format(distance))

    return distance


while True:
    distance = get_distance()
    time.sleep(0.05)
    print(distance)

    if distance >= 30:
        green_light()
    elif 30 > distance > 10:
        yellow_light()
    elif distance <= 10:
        red_light()



