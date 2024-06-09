# Overview

I wanted to make a TCP peer to server connection that allows for 2 users to connect to each other.

I made a client to server relationship using python and the sockets module. The server is started by python and binds to the ip of the host and a set port. The client is also started by python and uses sockets to connect to the server over the ip address.

I wrote this to gain more knowledge in the different types of networking connections and how python uses this to connect users.


[Software Demo Video]([http://youtube.link.goes.here](https://www.youtube.com/watch?v=ctiDHnA4aKc))

# Network Communication

{Describe the architecture that you used (client/server or peer-to-peer)}
I used a TCP socket in Python that sends things using binary and encodes and decodes the data based on the format being used. Sockets make the connection and allow the user to connect to other devices or bind to a port on the device.
{Identify if you are using TCP or UDP and what port numbers are used.}
I used TCP and port 5050 for the server and the same for the client with the port being an unused port, usually around 60764.
{Identify the format of messages being sent between the client and server or the messages sent between two peers.}
I used utf-8 format to encode and decode the data from the message.
# Development Environment

{Describe the tools that you used to develop the software}
I used visual studio code as my IDE and github to store my data. I also used python and local device ports and ip address.
{Describe the programming language that you used and any libraries.}
I used python with socket, threading, and queue modules to make the connections, handle multiple requests, and tranfer data.
# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Neural Nine Socket Tutorial]([http://url.link.goes.here](https://www.youtube.com/watch?v=qFVoMo6OMsQ&t=371s&ab_channel=NeuralNine))
* [Tech With Tim Socket Tutorial]([http://url.link.goes.here](https://www.youtube.com/watch?v=3QiPPX-KeSc&t=1749s&ab_channel=TechWithTim))

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* File Transfer
* Cleaner Entry and Exit of Server and Client
* UDP based, peer to peer
