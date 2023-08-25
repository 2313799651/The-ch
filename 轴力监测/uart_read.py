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
read_data2[7]=0x39

read_data3=bytearray(8)
read_data3[0]=0x03
read_data3[1]=0x03
read_data3[2]=0x00
read_data3[3]=0x00
read_data3[4]=0x00
read_data3[5]=0x01
read_data3[6]=0x85
read_data3[7]=0xE8

device_init1=bytearray(8)
device_init1[0]=0x01
device_init1[1]=0x06
device_init1[2]=0x00
device_init1[3]=0x11
device_init1[4]=0x00
device_init1[5]=0x01
device_init1[6]=0x18
device_init1[7]=0x0F

device_init2=bytearray(8)
device_init2[0]=0x02
device_init2[1]=0x06
device_init2[2]=0x00
device_init2[3]=0x11
device_init2[4]=0x00
device_init2[5]=0x01
device_init2[6]=0x18
device_init2[7]=0x3C

device_init3=bytearray(8)
device_init3[0]=0x03
device_init3[1]=0x06
device_init3[2]=0x00
device_init3[3]=0x11
device_init3[4]=0x00
device_init3[5]=0x01
device_init3[6]=0x18
device_init3[7]=0x0F

Tx=machine.Pin(7,Pin.OUT,value=1)
Rx=machine.Pin(9,Pin.IN, Pin.PULL_UP)
EN=machine.Pin(8,Pin.OUT)
uart = machine.UART(1, baudrate=9600, tx=7, rx=9)

def device_init:
    
    EN.value(1)
    time.sleep(0.1)
    uart.write(device_init1)
    time.sleep(0.01)
    EN.value(0)
    time.sleep(0.05)
    while uart.any()>0:
        rxData = uart.read()
        if len(rxData)>4:
            measure=0.00
            #print(rxData)
            measure += rxData[1] << 8
            measure += rxData[2]
            print(measure)
            print('设备1初始化成功')
             
    EN.value(1)
    time.sleep(0.1)
    uart.write(device_init2)
    time.sleep(0.01)
    EN.value(0)
    time.sleep(0.05)
    while uart.any()>0:
        rxData = uart.read()
        if len(rxData)>4:
            measure=0.00
            #print(rxData)
            measure += rxData[1] << 8
            measure += rxData[2]
            print(measure)
            print('设备2初始化成功')
            
    EN.value(1)
    time.sleep(0.1)
    uart.write(device_init3)
    time.sleep(0.01)
    EN.value(0)
    time.sleep(0.05)
    while uart.any()>0:
        rxData = uart.read()
        if len(rxData)>4:
            measure=0.00
            #print(rxData)
            measure += rxData[1] << 8
            measure += rxData[2]
            print(measure)
            print('设备3初始化成功')
            
def uart1_read():

    EN.value(1)
    time.sleep(0.1)
    uart.write(read_data1)
    time.sleep(0.01)
    EN.value(0)
    time.sleep(0.05)
    while uart.any()>0:
        rxData = uart.read()
        if len(rxData)>4:
            measure=0.00
            #print(rxData)
            measure += rxData[1] << 8
            measure += rxData[2]
            print(measure)

    try:
        pressure=0.00
        pressure=measure/10   
        print('接口1数据为：'+str(pressure))
        return(pressure)
    except NameError:
        print("NULL")
      


def uart2_read():
    
    EN.value(1)
    time.sleep(0.1)
    uart.write(read_data2)
    time.sleep(0.01)
    EN.value(0)
    time.sleep(0.05)
    while uart.any()>0:
        rxData = uart.read()
        if len(rxData)>4:
            measure=0.00
            #print(rxData)
            measure += rxData[1] << 8
            measure += rxData[2]
            print(measure)
    try:
        pressure=0.00
        pressure=measure/10   
        print('接口2数据为：'+str(pressure))
        #return(pressure)
    except NameError:
        print("NULL")
   

def uart3_read():
    
    EN.value(1)
    time.sleep(0.1)
    uart.write(read_data3)
    time.sleep(0.01)
    EN.value(0)
    time.sleep(0.05)
    while uart.any()>0:
        rxData = uart.read()
        if len(rxData)>4:
            measure=0.00
            #print(rxData)
            measure += rxData[1] << 8
            measure += rxData[2]
            print(measure)
    try:
        pressure=0.00
        pressure=measure/10   
        print('接口3数据为：'+str(pressure))
        #return(pressure)
    except NameError:
        print("NULL")
     


