from machine import UART,Pin
import time
import binascii
import os
import machine
import struct
import socket

Tx1=machine.Pin(4,Pin.OUT,value=1)
Rx1=machine.Pin(39,Pin.IN,Pin.PULL_UP)
gnd=machine.Pin(25,Pin.OUT,value=0)

uart1=UART(1, baudrate=38400,tx=19, rx=2)

uart2=UART(2, baudrate=9600,tx=4, rx=39)

Ranging=bytearray(5)
Ranging[0]=0xA5
Ranging[1]=0x5A
Ranging[2]=0x02
Ranging[3]=0x00
Ranging[4]=0xFD

MotorStepping=bytearray(8)
MotorStepping[0]=0xA5
MotorStepping[1]=0xFF
MotorStepping[2]=0x73
MotorStepping[3]=0x20
MotorStepping[4]=0x00
MotorStepping[5]=0x00
MotorStepping[6]=0x00
MotorStepping[7]=0x37

MotorRotate=bytearray(8)
MotorRotate[0]=0xA5
MotorRotate[1]=0xFF
MotorRotate[2]=0x73
MotorRotate[3]=0x00
MotorRotate[4]=0x19
MotorRotate[5]=0x00
MotorRotate[6]=0x00
MotorRotate[7]=0x30

SetSubdivision=bytearray(8)
SetSubdivision[0]=0xA5
SetSubdivision[1]=0xFF
SetSubdivision[2]=0x6D
SetSubdivision[3]=0x20
SetSubdivision[4]=0x00
SetSubdivision[5]=0x00
SetSubdivision[6]=0x00
SetSubdivision[7]=0x31

SetStartspeed=bytearray(8)
SetStartspeed[0]=0xA5
SetStartspeed[1]=0xFF
SetStartspeed[2]=0x4C
SetStartspeed[3]=0x58
SetStartspeed[4]=0x02
SetStartspeed[5]=0x00
SetStartspeed[6]=0x00
SetStartspeed[7]=0xB8

SetStopspeed=bytearray(8)
SetStopspeed[0]=0xA5
SetStopspeed[1]=0xFF
SetStopspeed[2]=0x53
SetStopspeed[3]=0x58
SetStopspeed[4]=0x02
SetStopspeed[5]=0x00
SetStopspeed[6]=0x00
SetStopspeed[7]=0xBF

Set_Hspeed=bytearray(8)
Set_Hspeed[0]=0xA5
Set_Hspeed[1]=0xFF
Set_Hspeed[2]=0x76
Set_Hspeed[3]=0xA0
Set_Hspeed[4]=0x0F
Set_Hspeed[5]=0x00
Set_Hspeed[6]=0x00
Set_Hspeed[7]=0xE2

Set_I=bytearray(8)
Set_I[0]=0xA5
Set_I[1]=0xFF
Set_I[2]=0x65
Set_I[3]=0x2C
Set_I[4]=0x01
Set_I[5]=0x00
Set_I[6]=0x00
Set_I[7]=0xFE

read_sta=bytearray(8)
read_sta[0]=0xA5
read_sta[1]=0xFF
read_sta[2]=0x63
read_sta[3]=0x00
read_sta[4]=0x00
read_sta[5]=0x00
read_sta[6]=0x00
read_sta[7]=0x07

Set_sta=bytearray(8)
Set_sta[0]=0xA5
Set_sta[1]=0xFF
Set_sta[2]=0x69
Set_sta[3]=0x00
Set_sta[4]=0x00
Set_sta[5]=0x00
Set_sta[6]=0x00
Set_sta[7]=0x0D

Set_origin=bytearray(8)
Set_origin[0]=0xA5
Set_origin[1]=0xFF
Set_origin[2]=0x69
Set_origin[3]=0x00
Set_origin[4]=0x00
Set_origin[5]=0x00
Set_origin[6]=0x00
Set_origin[7]=0x0D

measure=bytearray()
motor=bytearray()
h=0
data=[0]*205
angel=[0]*205

SERVER_HOST = '192.168.1.104'  # 网络接口
SERVER_PORT = 1234

# 创建TCP套接字并绑定地址
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))

# 开始监听连接
server_socket.listen(1)
print('Waiting for incoming connections...')

while True:
    # 接受客户端连接
    while True:
        
        try:
            client_socket, client_address = server_socket.accept()
            print('Connected to:', client_address)
            break 
        except OSError as e:
            time.sleep(1)
    try:
        # 处理客户端请求
        while True:
            # 接收客户端数据
            data = client_socket.recv(1024)
            if not data:
                # 客户端断开连接
                print('Client disconnected')
                break
            else:
                if data == b'init':
                    h=0
                    print("yifasong")
                    uart2.write(SetSubdivision)
                    time.sleep(0.5)
                    uart2.write(SetStartspeed)
                    time.sleep(0.5)
                    uart2.write(SetStopspeed)
                    time.sleep(0.5)
                    uart2.write(Set_Hspeed)
                    time.sleep(0.5)
                    uart2.write(Set_I)
                    time.sleep(0.5)
                    uart2.write(Set_sta)
                    time.sleep(0.1)
                    init_sta=0
                    c=0
                    while c==0:
                        uart2.write(read_sta)
                        time.sleep(0.1)
                        if uart2.any()>0:
                            measure=uart2.read()
                            if len(measure)>7:
                                init_sta += measure[6] << 24
                                init_sta += measure[5] << 16
                                init_sta += measure[4] << 8
                                init_sta += measure[3]
                                c=1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                    uart2.write(MotorRotate)
                    time.sleep(5)
                    client_socket.send("ok".encode())
                if data==b'start':
                    uart1.write(Ranging)
                    time.sleep(2)
                    measure_output=0
                    while uart1.any()>0:
                        measure=uart1.read()
                        measure_output += measure[3] << 24
                        measure_output += measure[4] << 16
                        measure_output += measure[5] << 8
                        measure_output += measure[6]
                    while measure_output==0 or measure_output>40000:
                        uart1.write(Ranging)
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
                    distance=str(measure_output)
                    angel=str(1.8*h)
                    SEND = f"{angel}:{distance}"
                    if h>=201:
                        h=1
                    else:
                        h=h+1
                        g=1
                        uart2.write(MotorStepping)
                        time.sleep(0.1)
                        while uart2.any()>0:
                            measure=uart2.read()
                            for i in range(0,len(measure)-3):
                                if measure[i]==165 and measure[i+1]==122 and measure[i+2]==255:
                                    g=0
                                    break
                        while g:
                            uart2.write(MotorStepping)
                            time.sleep(0.1)
                            while uart2.any()>0:
                                measure=uart2.read()
                                for i in range(0,len(measure)-3):
                                    if measure[i]==165 and measure[i+1]==122 and measure[i+2]==255:
                                        g=0
                                        break
                    client_socket.send(SEND.encode())
                if data==b'check':
                    c=0
                    while c==0:
                        uart2.write(read_sta)
                        time.sleep(0.1)
                        measure_output=0
                        if uart2.any()>0:
                            measure=uart2.read()
                            if len(measure)>7:
                                measure_output += measure[6] << 24
                                measure_output += measure[5] << 16
                                measure_output += measure[4] << 8
                                measure_output += measure[3]
                                c=1
                    def checksum(data):
                        return sum(data) & 0xff
                    error=abs(init_sta-measure_output)
                    print(error)
                    if error!=6400:
                        error=abs(6400-error)
                        print(error)
                        byte_array = struct.pack("<I", error)
                        print(byte_array)  # 输出结果为b'\x1a+<M'
                        Set_origin[0]=0xA5
                        Set_origin[1]=0xFF
                        Set_origin[2]=0x73
                        Set_origin[3]=byte_array[0]
                        Set_origin[4]=byte_array[1]
                        Set_origin[5]=byte_array[2]
                        Set_origin[6]=byte_array[3]
                        destination = bytearray(7)
                        destination[:] = Set_origin[0:6] 
                        p=checksum(destination)
                        Set_origin[7]=p
                        print(Set_origin)
                        uart2.write(Set_origin)
                        time.sleep(5)
                        init_sta=measure_output
                        h=1
                        #client_socket.send("ok".encode())
                    else:
                        h=1
    except:
        time.sleep(1)