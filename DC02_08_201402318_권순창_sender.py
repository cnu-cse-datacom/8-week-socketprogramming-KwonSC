import socket
import os

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip_addr = "192.168.0.71"
port = 9000

file_name=input("Input your file name : ")
file_size = os.path.getsize(file_name)

print("File Transmit Start....")
socket.sendto(file_name.encode(),(ip_addr, port))
socket.sendto(str(file_size).encode(),(ip_addr, port))

i = 1
fl=open(file_name,"rb")
data = fl.read(1024)

while (data):
    percent = 1024 * i / file_size * 100
    if (percent > 100) :
        print("current_size / total_size = ", file_size, "/", file_size, "100%")
    else:
        print("current_size / total_size = ", 1024*i, "/", file_size, percent, "%")
    if(socket.sendto(data,(ip_addr, port))):
        data = fl.read(1024)
        i = i + 1

print("ok")
print("file_send_end")
fl.close()