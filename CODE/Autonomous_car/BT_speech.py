#!/usr/bin/env python
import time
import serial
import RPi.GPIO as GPIO
import os
import RPi.GPIO as GPIO
import time

import telepot
bot = telepot.Bot('6081792684:AAFaUT2iMVW_sH035PU0okDPZfBBAJ1fGW8')

ser = serial.Serial(
  
   port='/dev/ttyS0',  #ttyAMA0 ttyS0
   baudrate = 9600,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#movement
IN1=27
IN2=22
IN3=23
IN4=24

#leveling
IN5=5
IN6=12

#filling
IN7=20
IN8=21

GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)

GPIO.setup(IN5,GPIO.OUT)
GPIO.setup(IN6,GPIO.OUT)
GPIO.setup(IN7,GPIO.OUT)
GPIO.setup(IN8,GPIO.OUT)

GPIO.output(IN1,False)
GPIO.output(IN2,False)
GPIO.output(IN3,False)
GPIO.output(IN4,False)

GPIO.output(IN5,False)
GPIO.output(IN6,False)
GPIO.output(IN7,False)
GPIO.output(IN8,False)
time.sleep(1)

def stop():
    print ("stop")
    GPIO.output(IN1,False)
    GPIO.output(IN2, False)
    GPIO.output(IN3,False)
    GPIO.output(IN4,False)
    time.sleep(1)

def forward():
    GPIO.output(IN1,False)
    GPIO.output(IN2, True)
    GPIO.output(IN3,False)
    GPIO.output(IN4,True)
    print ("Forward")
    time.sleep(1)

def backward():
    GPIO.output(IN1,True)
    GPIO.output(IN2, False)
    GPIO.output(IN3,True)
    GPIO.output(IN4,False)
    print ("backward")
    time.sleep(1)
    
def Filling():
    GPIO.output(IN7,False)
    GPIO.output(IN8, True)
    time.sleep(0.5)
    GPIO.output(IN7,False)
    GPIO.output(IN8,False)
    time.sleep(2)
    GPIO.output(IN7,True)
    GPIO.output(IN8, False)
    time.sleep(0.5)
    GPIO.output(IN7,False)
    GPIO.output(IN8,False)
    time.sleep(1)

def leveling_down():
    GPIO.output(IN5,False)
    GPIO.output(IN6, True)
    time.sleep(0.4)
    GPIO.output(IN5,False)
    GPIO.output(IN6,False)
    time.sleep(1)

def leveling_up():
    GPIO.output(IN5,True)
    GPIO.output(IN6, False)
    time.sleep(0.4)
    GPIO.output(IN5,False)
    GPIO.output(IN6,False)
    time.sleep(1)
    
while True:
   x=ser.readline()
   x = x.decode('UTF-8','ignore')
   print(x)
   
   if x == 'forward':
      forward()
   if x == 'backward':
      backward()
   if x == 'left':
       left()
   if x == 'right':
       right()
   if x == 'stop':
       stop()
   if x == 'filling':
       Filling()
   if x == 'leveling up':
       leveling_up()
   if x == 'leveling down':
       leveling_down()