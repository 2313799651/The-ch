from machine import UART,Pin
import time
import os
import machine
import uart_read

h=0
data1=[0]*201
data2=[0]*201
data3=[0]*201

rtc = machine.RTC()

while True:
    
    uart_read.uart1_read()
    time.sleep(0.1)
    uart_read.uart2_read()
    time.sleep(0.1)
    uart_read.uart3_read()
    time.sleep(0.1)
       
    zero=input("是否清零：y/n\n")
    if zero=='y':
        uart_read.device_init()
    else:
        break
    
while True:
    # Read time from terminal
    time_str = input("Enter time (MM:DD:HH): ")
    try:
        # Convert time string to tuple
        time_tuple = tuple(map(int, time_str.split(":")))
        # Set RTC time
        rtc.datetime((2023, time_tuple[0], time_tuple[1], 0,time_tuple[2],0,0,0))
        print("Time set successfully!")
        break
    except Exception as e:
        print("Invalid time format. Please enter time in MM:DD:HH format.")

while True:
    
    while h==60:
        
        if '1-1-zData' in os.listdir('/'):#新建文件夹
            print('1-1-zData exists')
        else:
            os.mkdir('/1-1-zData')

        files2 = os.listdir('/1-1-zData')
        f2=len(files2)
        print(f2)
        
        LTime = rtc.datetime()
        v = (str(LTime[0]) + "-" + str(LTime[1]) + "-" + str(LTime[2]) + "-" + str(LTime[4]))
        print(v)
        
        if f2<=240:
           file = open("/1-1-zData/1-1-"+v+".csv", "w")
           print("file establish")
           file.write('接口1'+','+'接口2'+','+'接口3'+'\n')  
           for i in range(0,h):
                file.write(str(data1[i])+","+str(data2[i])+","+str(data3[i])+"\n")
           file.close()
           print("Data written to CSV file")
           time.sleep(2)
           h=0
          
        else:
            while True:
                try:
                    for file in os.listdir('/1-1-zData'):
                        os.remove('/1-1-zData' + "/" + file)
                        time.sleep(1)
                    print("All files in Data deleted successfully!")    
                    break
                except OSError as e:
                    print("Error deleting files:", e)
                    time.sleep(5)

            file = open("/1-1-zData/1-1-"+v+".csv", "w")
            file.write('接口1'+','+'接口2'+','+'接口3'+'\n') 
            for i in range(0,h):
                file.write(str(data1[i])+","+str(data2[i])+","+str(data3[i])+"\n")
            file.close()
            print("Data written to CSV file")
            time.sleep(2)
            h=0
            
    data1[h]=uart_read.uart1_read()
    
    time.sleep(2)
    
    data2[h]=uart_read.uart2_read()
    
    time.sleep(2)
    
    data3[h]=uart_read.uart3_read()
   
    time.sleep(2)
    
    h=h+1
    time.sleep(35)
