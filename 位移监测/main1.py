from machine import UART,Pin,SPI
import time
import binascii
import os, spiSdcard
import machine

uart1=UART(1, baudrate=38400,tx=19, rx=2)
uart2=UART(2, baudrate=9600,tx=4, rx=39)

SD_CS = Pin(15)
spi=SPI(1,sck=Pin(14), mosi=Pin(13),miso=Pin(12))
spi.init()
sd = spiSdcard.SDCard(spi, SD_CS)
while True:
    try:
        vfs = os.VfsFat(sd)# fat挂载卡到⽬录下
        os.mount(sd,"/sd")
        files2 = os.listdir('/sd')
        f1=len(files2)+1
        os.mkdir('/sd/'+str(f1))
        break
    except OSError as e:
        time.sleep(2)

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
d=0

rtc = machine.RTC()
rtc.datetime((2023,05,00,00,00,00,00,00))


while True:
    
    while h==2:
        
        LTime = rtc.datetime()
        
        v=(str(LTime[0])+"-"+str(LTime[1])+'-'+str(LTime[4])+"-"+str(LTime[5]))
        while True:
            try:
                files2 = os.listdir('/sd/'+str(d+f1))
                f2=len(files2)
                break
            except OSError as e:
                time.sleep(2)
        
       111
        if f2<=72:
           
            while True:
                try:
                   with open("/sd/"+str(d+f1)+"1-1"+" "+v+".csv", "w") as file:
                       for i in range(0,h):
                            file.write(str(angel[i])+","+str(data[i])+"\n")
                       file.close()
                   break
                except OSError as e:
                    time.sleep(2)
           
            h=0
        else:
            d=d+1
            os.mkdir('/sd/'+str(d+f1))
            while True:
                try:
                   with open("/sd/"+str(d+f1)+"1-1"+" "+v+".csv", "w") as file:
                       for i in range(0,h):
                            file.write(str(angel[i])+","+str(data[i])+"\n")
                       file.close()
                   break
                except OSError as e:
                    time.sleep(2)
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
    
    time.sleep(3)




