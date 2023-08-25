import socket
import time
import uart_read2
# 设置服务器地址和端口
SERVER_HOST = '192.168.1.202'  # 网络接口
SERVER_PORT = 1234

# 创建TCP套接字并绑定地址
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))

# 开始监听连接
server_socket.listen(1)
print('Waiting for incoming connections...')

while True:
    # 接受客户端连接
    client_socket, client_address = server_socket.accept()
    print('Connected to:', client_address)
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
                    UART1_1,UART1_2,UART1_3,UART1_4 = uart_read2.uart1_read()
                    time.sleep(0.5)
                    UART2_1,UART2_2,UART2_3,UART2_4 = uart_read2.uart2_read()
                    time.sleep(0.5)
                    UART3_1,UART3_2,UART3_3,UART3_4 = uart_read2.uart3_read()
                    time.sleep(0.5)
                    
                    SEND = f"{UART1_1}:{UART1_2}:{UART1_3}:{UART1_4}:{UART2_1}:{UART2_2}:{UART2_3}:{UART2_4}:{UART3_1}:{UART3_2}:{UART3_3}:{UART3_4}"
                    client_socket.send(SEND.encode())
                if data == b'zero':
                    
                    uart_read2.device_init()
                    time.sleep(0.5)
                    
                    UART1_1,UART1_2,UART1_3,UART1_4 = uart_read2.uart1_read()
                    time.sleep(0.5)
                    UART2_1,UART2_2,UART2_3,UART2_4 = uart_read2.uart2_read()
                    time.sleep(0.5)
                    UART3_1,UART3_2,UART3_3,UART3_4 = uart_read2.uart3_read()
                    time.sleep(0.5)
                    
                    
                    SEND = f"{UART1_1}:{UART1_2}:{UART1_3}:{UART1_4}:{UART2_1}:{UART2_2}:{UART2_3}:{UART2_4}:{UART3_1}:{UART3_2}:{UART3_3}:{UART3_4}"
                    client_socket.send(SEND.encode())
                    
                if data == b'start':
                    #client_socket.send(b"start")
                    UART1_1,UART1_2,UART1_3,UART1_4 = uart_read2.uart1_read()
                    time.sleep(0.5)
                    UART2_1,UART2_2,UART2_3,UART2_4 = uart_read2.uart2_read()
                    time.sleep(0.5)
                    UART3_1,UART3_2,UART3_3,UART3_4 = uart_read2.uart3_read()
                    time.sleep(0.5)
                    
                    
                    SEND = f"{UART1_1}:{UART1_2}:{UART1_3}:{UART1_4}:{UART2_1}:{UART2_2}:{UART2_3}:{UART2_4}:{UART3_1}:{UART3_2}:{UART3_3}:{UART3_4}"
                    client_socket.send(SEND.encode())
                    #time.sleep(2)
    except:
        time.sleep(1)
