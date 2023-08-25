from machine import UART,Pin,SPI
import time
import binascii
import os, spiSdcard

import webrepl
import network

ap_if = network.WLAN(network.AP_IF)
ap_if.config(essid= '1-1' )
ap_if.active(True)
print(ap_if.ifconfig())

import uftpd
uftpd.restart()#启动uftpd，先打开再重启
webrepl.start(password="12345678")

uart1=UART(1, baudrate=38400,tx=19, rx=2)
uart2=UART(2, baudrate=9600,tx=4, rx=39)

SD_CS = Pin(15)
spi=SPI(1,sck=Pin(14), mosi=Pin(13),miso=Pin(12))
spi.init()
sd = spiSdcard.SDCard(spi, SD_CS)
vfs = os.VfsFat(sd)# fat挂载卡到⽬录下
os.mount(sd,"/sd")

#LTime=time.localtime()

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

measure=bytearray()
motor=bytearray()

h=0
data=[0]*201
angel=[0]*201

while True:
    
    while h==2:
        time.sleep(2)
        LTime=time.localtime()
        v=(str(LTime[0])+"-"+str(LTime[1])+"-"+str(LTime[2])+"-"+str(LTime[3])+"-"+str(LTime[4])+"-"+str(LTime[5])+"-"+str(LTime[6]))
        with open("/sd/"+str(v)+".csv", "w") as file:
            for i in range(0,h):
                file.write(str(angel[i])+","+str(data[i])+"\n")
            time.sleep(2)    
            file.close()
        h=0
       
    uart1.write(a)
    time.sleep(2)
    uart2.write(b)
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
    
    time.sleep(3)


'''
with open ("/sd/1.csv", "r") as file:
    m=file.read()
    print(m)
file.close()

dirs=os.listdir('/sd')
for file in dirs:   
    print(file)
'''
#缺复位、中断
