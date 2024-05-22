**INTRODUCTION**

In recent years, the development of embedded systems has surged, particularly with the advent of versatile and affordable microcontrollers like the Raspberry Pi Pico W. This project explores the implementation of a server-host communication system using two Raspberry Pi Pico W microcontrollers. The primary objective was to establish a reliable and efficient communication protocol between a server and a host terminal, enabling the exchange of messages. This system has potential applications in various domains, including home automation, remote monitoring, and IoT solutions.

**COMPONENTS**

The core components utilized in this project include two Raspberry Pi Pico W microcontrollers, each equipped with Wi-Fi capabilities for wireless communication. Additional components involved in the setup include a breadboard, connecting wires, button to represent a keyboard, power supply unit, and a computer for initial programming and monitoring. The software aspect was developed using MicroPython, a lightweight programming language suitable for microcontroller environments. Essential libraries such as network, socket, and uasyncio were employed to facilitate network communication and asynchronous operations.

**CIRCUIT DIAGRAM**

RSP Pico  |  OLED

16        |  CS

17        |  DC

18        |  SCK

19        |  MOSI

20        |  RST

RSP Pico  | BUTTON

13        | 1-Right

VCC       | 2-Left
![Capture](https://github.com/Aurah-P/Client-Server-Communication/assets/167772589/d1747a65-bc88-4d95-b286-9027578398ad)

**DISCUSSION**

The project commenced with the configuration of the Raspberry Pi Pico W microcontrollers, setting one as the server and the other as the host terminal. The server was programmed to establish a Wi-Fi network and listen for incoming connections. Upon connection, it could receive and process messages from the host. The host terminal, on the other hand, was designed to scan for the server's Wi-Fi network, connect to it, and send messages.
The implementation involved writing and deploying MicroPython scripts to both microcontrollers. The server script included code to set up the Wi-Fi access point, accept client connections, and handle incoming messages. The host script focused on connecting to the server's network and transmitting data. 
When connection is established in the server and the host terminal, one can send and receive messages from the other but it has to happen one at a time, this is called a half duplex type of communication. After sending a message, one has to wait until a message is received from the other. For this project, the message to be sent has already been configured and so the button is used as a send command

**CONCLUSION**

The project successfully demonstrated the capability of Raspberry Pi Pico W microcontrollers to establish a server-host communication system. The microcontrollers were able to send and receive messages reliably over a wireless network, highlighting their potential for various embedded system applications. The use of MicroPython and its networking libraries proved effective in creating a seamless communication protocol. Despite minor connectivity challenges, the overall system performance was robust and met the initial project objectives.

**RECOMMENDATIONS**

For future improvements, several enhancements can be considered. Firstly, implementing encryption for the transmitted data would enhance the security of the communication system, making it suitable for sensitive applications. Additionally, expanding the system to support multiple host terminals could provide more flexibility and scalability. Integrating additional sensors or actuators could further demonstrate the practical applications of such a communication setup. Finally, enhancing the system to be able to use a full duplex type of communication where any terminal can send and recieve messages at the same time. These recommendations aim to extend the functionality and applicability of the embedded communication system developed in this project.










