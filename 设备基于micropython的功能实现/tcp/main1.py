import socket
import time

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
                    UART1 = 0.5
                    #client_socket.send(str(UART1).encode)# uart_read.uart1_read()
                    time.sleep(0.5)
                    UART2 = 0.6
                    #client_socket.send(UART2)# uart_read.uart2_read()
                    time.sleep(0.5)
                    UART3 = 0.7
                    #client_socket.send(UART3)# uart_read.uart3_read()
                    time.sleep(0.5)
                    
                    SEND = f"{UART1}:{UART2}:{UART3}"
                    client_socket.send(SEND.encode())
                if data == b'zero':
                    
                    #uart_read.device_init()
                    time.sleep(0.5)
                    
                    UART1 = 0
                    #client_socket.send(str(UART1).encode)# uart_read.uart1_read()
                    time.sleep(0.5)
                    UART2 = 0
                    #client_socket.send(UART2)# uart_read.uart2_read()
                    time.sleep(0.5)
                    UART3 = 0
                    #client_socket.send(UART3)# uart_read.uart3_read()
                    time.sleep(0.5)
                    
                    SEND = f"{UART1}:{UART2}:{UART3}"
                    client_socket.send(SEND.encode())
                    
                if data == b'start':
                    #client_socket.send(b"start")
                    UART1 = 1  # uart_read.uart1_read()
                    time.sleep(0.1)
                    UART2 = 2  # uart_read.uart2_read()
                    time.sleep(0.1)
                    UART3 = 3  # uart_read.uart3_read()
                    time.sleep(0.1)
                    
                    SEND = f"{UART1}:{UART2}:{UART3}"
                    client_socket.send(SEND.encode())
                    time.sleep(2)
    except:
        time.sleep(1)
