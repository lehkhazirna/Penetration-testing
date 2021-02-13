import socket
target_host="127.0.0.1"
target_port=80

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.bind((target_host, target_port)) 
# A chunga mi hi double bracket a awm a ngai
# a chhan chu bind hian argument pakhat chiah a la thei. 
# bracket a awmloh chuan argument 2 a awm tihn a ani

req_message="AABBCC"
client.sendto(req_message.encode(),(target_host,target_port))
#sendto hi UDP bikah hman tur

data, addr = client.recvfrom(4096)

print(data)
print(addr)
# data recvfrom atang lo let ah hian b'AABBCC' tihin a awm nachhan chu
# b hi byte tihna ani
