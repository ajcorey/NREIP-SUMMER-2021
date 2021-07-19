#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

neckA = 14
neckB = 15

timeUp = 1
timeDown = 1
timeStopped = 2

GPIO.setup(neckA,GPIO.OUT)
GPIO.setup(neckB,GPIO.OUT)

def stop():
  GPIO.output(neckA,GPIO.LOW)
  GPIO.output(neckB,GPIO.LOW)

def up(timeToMove):
  GPIO.output(neckA,GPIO.LOW)
  GPIO.output(neckB,GPIO.HIGH)
  time.sleep(timeToMove)
  stop()

def down(timeToMove):
  GPIO.output(neckA,GPIO.HIGH)
  GPIO.output(neckB,GPIO.LOW)
  time.sleep(timeToMove)
  stop()  

stop()
for i in range(1):
  up(timeUp)
  time.sleep(timeStopped)
  down(timeDown)
  time.sleep(timeStopped)
  down(timeDown)
  time.sleep(timeStopped)
  up(timeUp)
  time.sleep(timeStopped)



