#!/usr/bin/env python3

import time
import serial
import pygame
import numpy as np

ser = serial.Serial(
  port='/dev/ttyS0',
  baudrate = 9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1
)

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((640, 480))

def setPitch(pitch):
  #-1000 , 1000
  if(pitch < -1000):
    pitch = -1000
  elif(pitch > 1000):
    pitch = 1000

  val=0
  if(pitch < 0):
    val = int(((pitch-1)/(-1000-1))*(0xBA-0xFF)+0xFF)
  elif(pitch >= 0):
    val = int(((pitch-0)/(1000-0))*(0x46-0x00)+0x00)

  s=str(hex(val))[2:].upper()
  if(len(s) < 2):
    s='0'+s

  return s

def setRudder(rudder):
  #-1000 , 1000
  if(rudder < -1000):
    rudder = -1000
  elif(rudder > 1000):
    rudder = 1000

  val=0
  if(rudder < 0):
    val = int(((rudder-1)/(-1000-1))*(0xBA-0xFF)+0xFF)
  elif(rudder >= 0):
    val = int(((rudder-0)/(1000-0))*(0x46-0x00)+0x00)

  s=str(hex(val))[2:].upper()
  if(len(s) < 2):
    s='0'+s

  return s

def setThrottle(throttle):
  #-1000 , 1000
  if(throttle < -1000):
    throttle = -1000
  elif(throttle > 1000):
    throttle = 1000

  val=0
  if(throttle < 0):
    val = int(((throttle-1)/(-1000-1))*(0xBE-0xFF)+0xFF)
  elif(throttle >= 0):
    val = int(((throttle-0)/(1000-0))*(0x42-0x00)+0x00)

  s=str(hex(val))[2:].upper()
  if(len(s) < 2):
    s='0'+s

  return s

def sendCommand(pitch,rudder,throttle):
  #write
  # #C(46-BA),(46-BA),(42-BE)\r
  # #C00,00,00\r center and neutral
  # #C(pitch),(rudder),(throttle)
  # pitch 01-46=nose down / FF-BA=nose up
  # rudder 01-46=nose left / FF-BA=nose right
  # throttle 01-42=forward / FF-BE=reverse
  pitch = setPitch(pitch)
  rudder = setRudder(rudder)
  throttle = setThrottle(throttle)

  s='#C'+pitch+','+rudder+','+throttle+'\r'
  ser.write(s.encode())
  print(s.encode())

def readResponse():
  r=' '
  x=b'_'
  while(x != b''):
    x=ser.read()
    r=r+x.decode()
  return r

vertical = 0
horizontal = 0
speed = 0
increment = 50

while 1:
  if(pygame.event.get(pygame.KEYDOWN)):
    if(pygame.key.get_pressed()[pygame.K_w]):
      vertical -= increment
    elif(pygame.key.get_pressed()[pygame.K_a]):
      horizontal += increment
    elif(pygame.key.get_pressed()[pygame.K_s]):
      vertical += increment
    elif(pygame.key.get_pressed()[pygame.K_d]):
      horizontal -= increment
    elif(pygame.key.get_pressed()[pygame.K_UP]):
      speed += increment
    elif(pygame.key.get_pressed()[pygame.K_DOWN]):
      speed -= increment
    elif(pygame.key.get_pressed()[pygame.K_SPACE]):
      vertical = 0
      horizontal = 0
      speed = 0

  if(vertical < -1000):
    vertical = -1000
  elif(vertical > 1000):
    vertical = 1000

  if(horizontal < -1000):
    horizontal = -1000
  elif(horizontal > 1000):
    horizontal = 1000

  if(speed < -1000):
    speed = -1000
  elif(speed > 1000):
    speed = 1000

  sendCommand(vertical,horizontal,speed)
  time.sleep(0.1)
  pygame.event.pump()
