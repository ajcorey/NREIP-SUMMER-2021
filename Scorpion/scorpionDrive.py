#!/usr/bin/python3

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#dir1 = 2
#pwm1 = 3
#dir2 = 4
#pwm2 = 17
rightPWM = 27
leftPWM = 19
freq = 350
#center is pwm(50)
#forward is pwmL(60+)
#reverse is pwmL(40-)
#forward is pwmR(40-)
#reverse is pwmR(60+)

timeForward = 3
timeOff = 2
timeReverse = 3

GPIO.setup(rightPWM, GPIO.OUT)
GPIO.setup(leftPWM,GPIO.OUT)
#GPIO.setup(dir1, GPIO.OUT)
#GPIO.setup(pwm1, GPIO.OUT)
#GPIO.setup(dir2, GPIO.OUT)
#GPIO.setup(pwm2, GPIO.OUT)

pwmR = GPIO.PWM(rightPWM,freq)
pwmL = GPIO.PWM(leftPWM,freq)

def stop():
  pwmR.stop()
  pwmL.stop()
  #GPIO.output(rightPWM, GPIO.LOW)
  #GPIO.output(leftPWM, GPIO.LOW)

def forward(timeToSleep):
  for i in range(50, 100, 5):
    pwmR.start(i)
  #pwmL.start(55)
  #GPIO.output(dir1, GPIO.HIGH)
  #GPIO.output(pwm1, GPIO.HIGH)
  #GPIO.output(dir2, GPIO.HIGH)
  #GPIO.output(pwm2, GPIO.HIGH)
  time.sleep(timeToSleep)
  stop()

def reverse(timeToSleep):
  for i in range(50, 0, -5):
    pwmR.start(i)
  #pwmL.start(45)
  #GPIO.output(dir1, GPIO.LOW)
  #GPIO.output(pwm1, GPIO.HIGH)
  #GPIO.output(dir2, GPIO.LOW)
  #GPIO.output(pwm2, GPIO.HIGH)
  time.sleep(timeToSleep)
  stop()

for i in range(2):
  forward(timeForward)
  time.sleep(timeOff)
  reverse(timeReverse)
  time.sleep(timeOff)


exit()
