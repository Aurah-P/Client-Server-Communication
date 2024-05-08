import socket
import network
import utime
from ssd1306 import SSD1306_SPI
import framebuf
from machine import Pin,SPI

spi =SPI(0, 100000, mosi=Pin(19), sck=Pin(18))
oled = SSD1306_SPI(128, 64, spi, Pin(17),Pin(20), Pin(16))
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("GEARBOX MEMBERS", "Members@Gearbox")
oled.fill(0)
oled.show()
oled.text("Initialising Server..",0,0)
oled.show()
utime.sleep(1.5)
while wifi.isconnected()== False:
    oled.fill(0)
    oled.show()
    oled.text("Waiting for connection",0,0)
    oled.show()
    utime.sleep(1)
wifiInfo=wifi.ifconfig()
ServerIP=wifiInfo[0]
ServerPort = 2222
bufferSize = 1024
UDPServer = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
UDPServer.bind((ServerIP,ServerPort))
clientAddress = ("192.168.0.10", 2222)
oled.fill(0)
oled.show()
oled.text("Connected",0,0)
oled.text(ServerIP, 0, 20)
oled.show()
utime.sleep(1)
while True:
    message,address = UDPServer.recvfrom(bufferSize)
    messageDecoded = message.decode("utf-8")
    oled.fill(0)
    oled.show()
    print("Them: " + messageDecoded)
    oled.text("Them: ",0,0)
    oled.text(messageDecoded, 0, 20)
    oled.show()
    utime.sleep(1)
    cmd = input("You: ")
    cmdEncoded = cmd.encode("utf-8")
    UDPServer.sendto(cmdEncoded, clientAddress)
    
    
