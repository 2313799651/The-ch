# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import ConnectWiFi

ConnectWiFi.connect_wifi()

import webrepl
webrepl.start(password="12345678")

import uftpd
#uftpd.restart()#启动uftpd，先打开再重启



