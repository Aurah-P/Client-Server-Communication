import socket
from ssd1306 import SSD1306_SPI
import framebuf
from machine import Pin,SPI
import network
import utime

button = Pin(13, Pin.IN, Pin.PULL_DOWN)
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("GEARBOX MEMBERS", "Members@Gearbox")
spi =SPI(0, 100000, mosi=Pin(19), sck=Pin(18))
oled = SSD1306_SPI(128, 64, spi, Pin(17),Pin(20), Pin(16))

serverAddress = ("192.168.0.49", 2222)
oled.fill(0)
oled.show()
oled.text("Initialising Client..",0,0)
oled.show()
utime.sleep(1.5)

while wifi.isconnected()== False:
    oled.fill(0)
    oled.show()
    oled.text("Waiting for connection",0,0)
    oled.show()
    print("No connection")
    utime.sleep(1)
wifiInfo=wifi.ifconfig()
ClientIP=wifiInfo[0]
ClientPort = 2222
bufferSize = 1024
UDPClient=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
UDPClient.bind((ClientIP,ClientPort))
oled.fill(0)
oled.show()
oled.text("Client Connected",0,0)
oled.text(ClientIP, 0, 15)
print(ClientIP)
oled.show()
while True:
    if button.value():
        ms= "Hello"
        
    else:
        ms="Typing..."
    
    msEncoded=ms.encode("utf-8")
    UDPClient.sendto(msEncoded, serverAddress)
    message,address = UDPClient.recvfrom(bufferSize)
    messageDecoded = message.decode("utf-8")
    oled.fill(0)
    oled.show()
    oled.text("You: ", 0,0)
    oled.text(ms, 40,0)
    oled.show()
    oled.text("Them: ",0,15)
    oled.text(messageDecoded, 40, 15)
    print("Them:" + messageDecoded)
    oled.show()
    utime.sleep(0.5)
    

