import socket
'''
import network
import utime
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("GEARBOX MEMBERS", "Members@Gearbox")
'''
serverAddress = ("192.168.0.26", 2222)
'''
while wifi.isconnected()== False:
    #oled.fill(0)
    #oled.show()
    #oled.text("Waiting for connection",0,0)
    #oled.show()
    print("No connection")
    utime.sleep(1)
wifiInfo=wifi.ifconfig()
ClientIP=wifiInfo[0]
'''
ClientIP = "192.168.0.10"
ClientPort = 2222
bufferSize = 1024
UDPClient=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
UDPClient.bind((ClientIP,ClientPort))
while True:
    cmd = input("You: ")
    cmdEncoded=cmd.encode("utf-8")
    UDPClient.sendto(cmdEncoded, serverAddress)
    message,address = UDPClient.recvfrom(bufferSize)
    messageDecoded = message.decode("utf-8")
    print("Them:" + messageDecoded)