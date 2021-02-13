import socket;
target_host= "google.com"
target_port=80

#1. socket object siam phawt tur
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#2. Client connect tur
client.connect((target_host,target_port))

# data send chhin
request = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
client.send(request.encode())

#recieve data
response = client.recv(4096)

print (response)
