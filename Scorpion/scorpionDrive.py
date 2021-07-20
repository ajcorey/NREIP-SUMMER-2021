#!/usr/bin/python3

import time
import RPi.GPIO as GPIO
from adafruit_blinka.board.raspberrypi.pico import LED
import adafruit_pca9685
import board




# PWM Stuff
#I2C address for the PWM driver board retrieved automatically
i2c_pwm = board.I2C()
pwm = adafruit_pca9685.PCA9685(i2c_pwm)

pwm.frequency = 350

#GPIO.setmode(GPIO.BCM)



rightPWM = 0
leftPWM = 2

#Turn off warnings about pins being already configured
#GPIO.setwarnings(False) 

#GPIO.setup(rightPWM, GPIO.OUT)
#GPIO.setup(leftPWM,GPIO.OUT)



def stop():
  #GPIO.output(,GPIO.HIGH)
  #GPIO.output(BL2,GPIO.HIGH)
  pwm.channels[rightPWM].duty_cycle = 0xFFFF
  pwm.channels[leftPWM].duty_cycle = 0xFFFF
  #GPIO.output(16,GPIO.HIGH)

def forward(timeToSleep):
  for i in range(50, 100, 5):
    pwm.channels[rightPWM].duty_cycle = abs(i)
    time.sleep(0.25)
  print("forwarded")
  stop()

def reverse(timeToSleep):
  for i in range(50, 0, -5):
    pwm.channels[rightPWM].duty_cycle = abs(i)
    time.sleep(0.25)
  print("reversed")
  stop()

# for i in range(1):
#   # forward(2)
#   # reverse(2)

pwm.channels[rightPWM].duty_cycle = 0xFFFF
time.sleep(5)
pwm.channels[rightPWM].duty_cycle = 0x0000


exit()
