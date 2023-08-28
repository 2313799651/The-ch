def connect_wifi():
import network

    station.active(True)
    station.ifconfig((ip_address, subnet_mask, gateway_address, dns_server))

    station.connect(ssid, password)

    while station.isconnected() == False:
        pass
    #station.ifconfig((ip_address, subnet_mask, gateway_address, dns_server))

    print("Connection successful")

    import webrepl
    webrepl.start(password="12345678")

    import uftpd
    #uftpd.restart()#启动uftpd，先打开再重启