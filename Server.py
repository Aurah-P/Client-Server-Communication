import socket
import network
import utime
from ssd1306 import SSD1306_SPI
import framebuf
from machine import Pin,SPI
button = Pin(13, Pin.IN, Pin.PULL_DOWN)
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
clientAddress = ("192.168.0.26", 2222)
oled.fill(0)
oled.show()
oled.text("Connected",0,0)
print("Connected" + ServerIP)
oled.text(ServerIP, 0, 20)
oled.show()
utime.sleep(1)
while True:
    message,address = UDPServer.recvfrom(bufferSize)
    messageDecoded = message.decode("utf-8")
    oled.fill(0)
    oled.show()
    oled.text("Them: ",0,0)
    oled.text(messageDecoded, 40, 0)
    oled.show()
    #utime.sleep(1)
    if button.value(): #when button is pressed send the following message
        cm = "Hello too"
    else:
        cm = "Typing..."
    oled.text("You: ", 0,15)
    oled.text(cm, 40,15)
    oled.show()
    cmEncoded = cm.encode("utf-8")
    UDPServer.sendto(cmEncoded, clientAddress)
    #utime.sleep(1)
    


