from machine import UART,Pin
import time
import os
import machine

rxData=bytearray(8)

read_data1=bytearray(8)
read_data1[0]=0x01
read_data1[1]=0x03
read_data1[2]=0x00
read_data1[3]=0x00
read_data1[4]=0x00
read_data1[5]=0x01
read_data1[6]=0x84
read_data1[7]=0x0A

read_data2=bytearray(8)
read_data2[0]=0x02
read_data2[1]=0x03
read_data2[2]=0x00
read_data2[3]=0x00
read_data2[4]=0x00
read_data2[5]=0x01
read_data2[6]=0x84
read_data2[7]=0x0A

read_data3=bytearray(8)
read_data3[0]=0x03
read_data3[1]=0x03
read_data3[2]=0x00
read_data3[3]=0x00
read_data3[4]=0x00
read_data3[5]=0x01
read_data3[6]=0x84
read_data3[7]=0x0A

Set_address2=bytearray(8)
Set_address2[0]=0x01
Set_address2[1]=0x06
Set_address2[2]=0x00
Set_address2[3]=0x06
Set_address2[4]=0x00
Set_address2[5]=0x02
Set_address2[6]=0xE8
Set_address2[7]=0x0A

Set_address3=bytearray(8)
Set_address3[0]=0x01
Set_address3[1]=0x06
Set_address3[2]=0x00
Set_address3[3]=0x06
Set_address3[4]=0x00
Set_address3[5]=0x03
Set_address3[6]=0x29
Set_address3[7]=0xCA

Tx=machine.Pin(7,Pin.OUT,value=1)
Rx=machine.Pin(9,Pin.IN, Pin.PULL_UP)
EN=machine.Pin(8,Pin.OUT)
uart = machine.UART(1, baudrate=9600, tx=7, rx=9)

while True:
    
    EN.value(1)
    time.sleep(0.5)
    uart.write(s)                                                                                                                             
    time.sleep(0.01)
    EN.value(0)
    time.sleep(0.05)
    while uart.any()>0:
        measure=0.00
        rxData = uart.read()
        print(len(rxData))
        print(rxData )
        measure += rxData[1] << 8
        measure += rxData[2]
        print(measure)

    time.sleep(1)

