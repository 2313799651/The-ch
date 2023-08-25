from machine import UART,Pin,SPI
import time
import binascii
import os, spiSdcard
import machine

uart1=UART(1, baudrate=38400,tx=19, rx=2)
uart2=UART(2, baudrate=9600,tx=4, rx=39)
'''
复制到boot.py
import network

ap_if = network.WLAN(network.AP_IF)
ap_if.config(essid= '1-1' )
ap_if.active(True)
print(ap_if.ifconfig())

import webrepl
webrepl.start(password="12345678")

import uftpd
#uftpd.restart()#启动uftpd，先打开再重启
'''
a=bytearray(5)
a[0]=0xA5
a[1]=0x5A
a[2]=0x02
a[3]=0x00
a[4]=0xFD

b=bytearray(8)
b[0]=0xA5
b[1]=0xFF
b[2]=0x73
b[3]=0x20
b[4]=0x00
b[5]=0x00
b[6]=0x00
b[7]=0x37

c=bytearray(8)
c[0]=0xA5
c[1]=0xFF
c[2]=0x73
c[3]=0x00
c[4]=0x19
c[5]=0x00
c[6]=0x00
c[7]=0x99


measure=bytearray()
motor=bytearray()

h=0
data=[0]*201
angel=[0]*201


#rtc = machine.RTC()
#rtc.datetime((2023,00,00,00,00,00,00,00))

uart2.write(c)

while True:
    
    while h==200:
        
        if '1-1Data' in os.listdir('/'):
            print('"1-1Data" exists')
        else:
            os.mkdir('/1-1Data')

        files2 = os.listdir('/1-1Data')
        f2=len(files2)
        print(f2)
      
        if f2<=240:
           file = open("/1-1Data/1-1-"+str(f2+1)+".csv", "w")
           print("file establish")
           for i in range(0,h):
                file.write(str(angel[i])+","+str(data[i])+"\n")
           file.close()
           print("Data written to CSV file")
           time.sleep(2)
           h=0
           uart2.write(c)
        else:
            while True:
                try:
                    for file in os.listdir('/1-1Data'):
                        os.remove('/1-1Data' + "/" + file)
                        time.sleep(1)
                    print("All files in Data deleted successfully!")    
                    break
                except OSError as e:
                    print("Error deleting files:", e)
                    time.sleep(5)

            file = open("/1-1Data/1-1-1"+".csv", "w")
            for i in range(0,h):
              file.write(str(angel[i])+","+str(data[i])+"\n")
            file.close()
            print("Data written to CSV file")
            time.sleep(2)
            h=0
            uart2.write(c)
    uart1.write(a)
    time.sleep(2)
    measure_output=0
    while uart1.any()>0:
        measure=uart1.read()
        measure_output += measure[3] << 24;
        measure_output += measure[4] << 16;
        measure_output += measure[5] << 8;
        measure_output += measure[6];
    while measure_output==0 or measure_output>40000:
        uart2.write(a)
        time.sleep(2)
        measure_output=0
        while uart1.any()>0:
            measure=uart1.read()
            measure_output += measure[3] << 24;
            measure_output += measure[4] << 16;
            measure_output += measure[5] << 8;
            measure_output += measure[6];
    print(measure_output)
    print(h)
    data[h]=measure_output
    angel[h]=1.8*h
    h=h+1
    uart2.write(b)
    time.sleep(16)





