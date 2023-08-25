from machine import UART,Pin
import time
import os
import machine

rxData=bytearray(8)

c=bytearray(8)
c[0]=0x01
c[1]=0x06
c[2]=0x00
c[3]=0x00
c[4]=0x00
c[5]=0x01
c[6]=0x48
c[7]=0x0A

Set_address2=bytearray(8)
Set_address2[0]=0x01
Set_address2[1]=0x06
Set_address2[2]=0x00
Set_address2[3]=0x00
Set_address2[4]=0x00
Set_address2[5]=0x02
Set_address2[6]=0x08
Set_address2[7]=0x0B

Set_address3=bytearray(8)
Set_address3[0]=0x01
Set_address3[1]=0x06
Set_address3[2]=0x00
Set_address3[3]=0x00
Set_address3[4]=0x00
Set_address3[5]=0x03
Set_address3[6]=0xC9
Set_address3[7]=0xCB


Tx=machine.Pin(7,Pin.OUT,value=1)
Rx=machine.Pin(9,Pin.IN, Pin.PULL_UP)
EN=machine.Pin(8,Pin.OUT)
uart = machine.UART(1, baudrate=9600, tx=7, rx=9)

while True:

    EN.value(1)
    time.sleep(0.5)
    uart.write(Set_address2 )                                                                                                                             
    time.sleep(0.01)
    EN.value(0)
    time.sleep(0.05)
    while uart.any()>0:
        measure=0.00
        rxData = uart.read()
        if len(rxData)>5
            print(rxData)
            measure += rxData[3] << 8
            measure += rxData[4]
            print(measure)

    time.sleep(1)
