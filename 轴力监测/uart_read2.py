from machine import UART,Pin
import time
import os
import machine

device_init1=bytearray(8)
device_init1[0]=0x01
device_init1[1]=0x05
device_init1[2]=0x00
device_init1[3]=0x68
device_init1[4]=0xff
device_init1[5]=0x00
device_init1[6]=0x0d
device_init1[7]=0xe6

device_init2=bytearray(8)
device_init2[0]=0x02
device_init2[1]=0x05
device_init2[2]=0x00
device_init2[3]=0x68
device_init2[4]=0xff
device_init2[5]=0x00
device_init2[6]=0x0d
device_init2[7]=0xd5

device_init3=bytearray(8)
device_init3[0]=0x03
device_init3[1]=0x05
device_init3[2]=0x00
device_init3[3]=0x68
device_init3[4]=0xff
device_init3[5]=0x00
device_init3[6]=0x0c
device_init3[7]=0x04

read_data1=bytearray(8)
read_data1[0]=0x01
read_data1[1]=0x03
read_data1[2]=0x01
read_data1[3]=0xf4
read_data1[4]=0x00
read_data1[5]=0x08
read_data1[6]=0x04
read_data1[7]=0x02

read_data2=bytearray(8)
read_data2[0]=0x02
read_data2[1]=0x03
read_data2[2]=0x01
read_data2[3]=0xf4
read_data2[4]=0x00
read_data2[5]=0x08
read_data2[6]=0x04
read_data2[7]=0x31

read_data3=bytearray(8)
read_data3[0]=0x04
read_data3[1]=0x03
read_data3[2]=0x01
read_data3[3]=0xf4
read_data3[4]=0x00
read_data3[5]=0x08
read_data3[6]=0x04
read_data3[7]=0x57

rxData=b""

Tx=machine.Pin(7,Pin.OUT,value=1)
Rx=machine.Pin(9,Pin.IN, Pin.PULL_UP)
EN=machine.Pin(8,Pin.OUT)
uart = machine.UART(1, baudrate=19200, tx=7, rx=9)

def device_init():

    EN.value(1)
    time.sleep(0.01)

    uart.write(device_init1)
    time.sleep(0.1)

    uart.write(device_init2)
    time.sleep(0.1)

    uart.write(device_init3)
    time.sleep(0.1)

    print('设备初始化成功')
def uart1_read():
    c=0
    while c==0:
        EN.value(1)
        time.sleep(0.01)
        
        uart.write(read_data1)
        time.sleep(0.0041)
        EN.value(0)
        time.sleep(0.2)
        if uart.any()>0:
            rxData = uart.read()
            if len(rxData)>18:
                if len(rxData)==21:
                    c=1
                    print(rxData)
                    measure1=0.00
                    measure2=0.00
                    measure3=0.00
                    measure4=0.00
                    measure1 += rxData[5] << 8
                    measure1 += rxData[6]
                    measure2 += rxData[9] << 8
                    measure2 += rxData[10]
                    measure3 += rxData[13] << 8
                    measure3 += rxData[14]
                    measure4 += rxData[17] << 8
                    measure4 += rxData[18]
                time.sleep(0.5)
                #print(measure)
                if uart.any()>0:
                    rxData = uart.read()
            else:
                c=1
        else:
            c=1
    try:
        pressure1=0.00
        pressure2=0.00
        pressure3=0.00
        pressure4=0.00
        
        pressure1=measure1/10
        pressure2=measure2/10
        pressure3=measure3/10
        pressure4=measure4/10
        
        print('接口1-1数据为：'+str(pressure1)+'\n')
        print('接口1-2数据为：'+str(pressure2)+'\n')
        print('接口1-3数据为：'+str(pressure3)+'\n')
        print('接口1-4数据为：'+str(pressure4)+'\n')
        
        return str(pressure1)+":"+str(pressure2)+":"+str(pressure3)+":"+str(pressure4)
    except NameError:
        print("NULL")
        return "-1:-1:-1:-1"
def uart2_read():
    c=0
    while c==0:
        EN.value(1)
        time.sleep(0.01)
        
        uart.write(read_data2)
        time.sleep(0.0041)
        EN.value(0)
        time.sleep(0.2)
        while uart.any()>0:
            rxData = uart.read()
            if len(rxData)>18:
                if len(rxData)==21:
                    c=1
                    print(rxData)
                    measure1=0.00
                    measure2=0.00
                    measure3=0.00
                    measure4=0.00
                    measure1 += rxData[5] << 8
                    measure1 += rxData[6]
                    measure2 += rxData[9] << 8
                    measure2 += rxData[10]
                    measure3 += rxData[13] << 8
                    measure3 += rxData[14]
                    measure4 += rxData[17] << 8
                    measure4 += rxData[18]
                time.sleep(0.5)
                #print(measure)
                if uart.any()>0:
                    rxData = uart.read()
            else:
                c=1
    try:
        pressure1=0.00
        pressure2=0.00
        pressure3=0.00
        pressure4=0.00
        
        pressure1=measure1/10
        pressure2=measure2/10
        pressure3=measure3/10
        pressure4=measure4/10
        
        print('接口2-1数据为：'+str(pressure1)+'\n')
        print('接口2-2数据为：'+str(pressure2)+'\n')
        print('接口2-3数据为：'+str(pressure3)+'\n')
        print('接口2-4数据为：'+str(pressure4)+'\n')
        return str(pressure1)+":"+str(pressure2)+":"+str(pressure3)+":"+str(pressure4)
    except NameError:
        print("NULL")
        return "-1:-1:-1:-1"

def uart3_read():
    c=0
    while c==0:
        EN.value(1)
        time.sleep(0.01)
        
        uart.write(read_data3)
        time.sleep(0.0041)
        EN.value(0)
        time.sleep(0.2)
        while uart.any()>0:
            rxData = uart.read()
            if len(rxData)>18:
                if len(rxData)==21:
                    c=1
                    print(rxData)
                    measure1=0.00
                    measure2=0.00
                    measure3=0.00
                    measure4=0.00
                    measure1 += rxData[5] << 8
                    measure1 += rxData[6]
                    measure2 += rxData[9] << 8
                    measure2 += rxData[10]
                    measure3 += rxData[13] << 8
                    measure3 += rxData[14]
                    measure4 += rxData[17] << 8
                    measure4 += rxData[18]
                time.sleep(0.5)
                #print(measure)
                if uart.any()>0:
                    rxData = uart.read()
            else:
                c=1
    try:
        pressure1=0.00
        pressure2=0.00
        pressure3=0.00
        pressure4=0.00
        
        pressure1=measure1/10
        pressure2=measure2/10
        pressure3=measure3/10
        pressure4=measure4/10
        
        print('接口3-1数据为：'+str(pressure1)+'\n')
        print('接口3-2数据为：'+str(pressure2)+'\n')
        print('接口3-3数据为：'+str(pressure3)+'\n')
        print('接口3-4数据为：'+str(pressure4)+'\n')
        return str(pressure1)+":"+str(pressure2)+":"+str(pressure3)+":"+str(pressure4)
    except NameError:
        print("NULL")
        return "-1:-1:-1:-1"
device_init()
while True:
    uart2=uart2_read()
    time.sleep(2)

