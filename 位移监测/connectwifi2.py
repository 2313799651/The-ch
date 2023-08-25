import network

ssid = "1-1"
password =  "mining514"

ip_address = "192.168.1.101"  # 将此替换为您要使用的IP地址
subnet_mask = "255.255.255.0"  # 将此替换为您的子网掩码
gateway_address = "192.168.1.194"  # 将此替换为您的网关地址
dns_server = "8.8.8.8"

station = network.WLAN(network.STA_IF)

station.active(True)
station.ifconfig((ip_address, subnet_mask, gateway_address, dns_server))

station.connect(ssid, password)

while station.isconnected() == False:
    pass
#station.ifconfig((ip_address, subnet_mask, gateway_address, dns_server))

print("Connection successful")

import uftpd
#(ip_address, subnet_mask, gateway_address, dns_server)