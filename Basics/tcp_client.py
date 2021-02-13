import socket;
target_host= "google.com"
target_port=80 # 80 hi web server a HTTP port pangai ani.

#1. socket object siam phawt tur

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# AF_INET hian IPV4 ani tihna ani a.
# SOCK_STREAM hian TCP client ani dawn tihna ani


#2. Client connect tur
client.connect((target_host,target_port))

# data send chhin
request = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
# A chunga string hi direct a hnuai mi anga ziah hi chuan
# client.send(("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"))
# A object hi byte kan duh a mahse a return chu string ani dawn a
# chuvangin byte anga return dawn chuan a string.encode() hman tur

client.send(request.encode()) 

# Recieve data
response = client.recv(4096) 

# 4096 hi a data recive tur size byte ani
# hei hi 2 power ani tur ani 

print (response)
