from machine import UART,Pin
import time
import os
import machine

rxData=bytearray(8)

d1=bytearray(8)
d1[0]=0x01
d1[1]=0x03
d1[2]=0x00
d1[3]=0x04
d1[4]=0x00
d1[5]=0x01
d1[6]=0xC5
d1[7]=0xCB

e1=bytearray(8)
e1[0]=0x01
e1[1]=0x03
e1[2]=0x00
e1[3]=0x03
e1[4]=0x00
e1[5]=0x01
e1[6]=0x74
e1[7]=0x0A

d2=bytearray(8)
d2[0]=0x02
d2[1]=0x03
d2[2]=0x00
d2[3]=0x04
d2[4]=0x00
d2[5]=0x01
d2[6]=0xC5
d2[7]=0xF8

e2=bytearray(8)
e2[0]=0x02
e2[1]=0x03
e2[2]=0x00
e2[3]=0x03
e2[4]=0x00
e2[5]=0x01
e2[6]=0x74
e2[7]=0x39

d3=bytearray(8)
d3[0]=0x03
d3[1]=0x03
d3[2]=0x00
d3[3]=0x04
d3[4]=0x00
d3[5]=0x01
d3[6]=0xC4
d3[7]=0x29

e3=bytearray(8)
e3[0]=0x03
e3[1]=0x03
e3[2]=0x00
e3[3]=0x03
e3[4]=0x00
e3[5]=0x01
e3[6]=0x75
e3[7]=0xE8

Tx=machine.Pin(7,Pin.OUT,value=1)
Rx=machine.Pin(9,Pin.IN, Pin.PULL_UP)
EN=machine.Pin(8,Pin.OUT)
uart = machine.UART(1, baudrate=9600, tx=7, rx=9)


def uart1_read():

    EN.value(1)
    time.sleep(0.1)
    uart.write(d1)
    time.sleep(0.008)
    EN.value(0)
    time.sleep(0.5)
    while uart.any()>0:
        rxData1 = uart.read()
        if len(rxData1)>5:
            measure=0.00
        #print(rxData1)
            measure += rxData1[3] << 8
            measure += rxData1[4]
            print(measure)
    
    time.sleep(0.5)

    EN.value(1)
    time.sleep(0.1)
    uart.write(e1)
    time.sleep(0.01)
    EN.value(0)
    time.sleep(0.5)
    while uart.any()>0:
        rxData2 = uart.read()
        #print(rxData2)
        if len(rxData2)>5:
            dot=0
            dot += rxData2[3] << 8
            dot += rxData2[4]
            print(dot)
            time.sleep(0.5)
        if uart.any()>0:
            rxData2 = uart.read()
            
    try:
        pressure=0.00
        pressure=measure/(10**dot)   
        print('接口1数据为：'+str(pressure))
        return(pressure)
    except NameError:
        print("NULL")
      


def uart2_read():
    
    EN.value(1)
    time.sleep(0.1)
    uart.write(d2)
    time.sleep(0.008)
    EN.value(0)
    time.sleep(0.5)
    while uart.any()>0:
        rxData1 = uart.read()
        if len(rxData1)>5:
            measure=0.00
        #print(rxData1)
            measure += rxData1[3] << 8
            measure += rxData1[4]
            print(measure)
    
    time.sleep(0.5)

    EN.value(1)
    time.sleep(0.1)
    uart.write(e2)
    time.sleep(0.01)
    EN.value(0)
    time.sleep(0.5)
    while uart.any()>0:
        rxData2 = uart.read()
        #print(rxData2)
        if len(rxData2)>5:
            dot=0
            dot += rxData2[3] << 8
            dot += rxData2[4]
            print(dot)
            time.sleep(0.5)
        if uart.any()>0:
            rxData2 = uart.read()
            
    try:
        pressure=0.00
        pressure=measure/(10**dot)   
        print('接口2数据为：'+str(pressure))
        #return(pressure)
    except NameError:
        print("NULL")
   

def uart3_read():
    
    EN.value(1)
    time.sleep(0.1)
    uart.write(d3)
    time.sleep(0.008)
    EN.value(0)
    time.sleep(0.5)
    while uart.any()>0:
        rxData1 = uart.read()
        if len(rxData1)>5:
            measure=0.00
        #print(rxData1)
            measure += rxData1[3] << 8
            measure += rxData1[4]
            print(measure)
    
    time.sleep(0.5)

    EN.value(1)
    time.sleep(0.1)
    uart.write(e3)
    time.sleep(0.01)
    EN.value(0)
    time.sleep(0.5)
    while uart.any()>0:
        rxData2 = uart.read()
        #print(rxData2)
        if len(rxData2)>5:
            dot=0
            dot += rxData2[3] << 8
            dot += rxData2[4]
            print(dot)
            time.sleep(0.5)
        if uart.any()>0:
            rxData2 = uart.read()
    try:
        pressure=0.00
        pressure=measure/(10**dot)   
        print('接口3数据为：'+str(pressure))
        #return(pressure)
    except NameError:
        print("NULL")
     


