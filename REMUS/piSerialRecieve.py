#!/usr/bin/env python3

import time
import serial

ser = serial.Serial(
  port='/dev/ttyS0',
  baudrate = 9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1
)

counter=0

while 1:
  #read
  x=ser.readline()
  print (x.decode())
  print("__")
