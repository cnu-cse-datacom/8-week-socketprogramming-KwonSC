import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 9000))

data, addr = server_socket.recvfrom(1024)
print("file recv start from ", addr[0])
print(data)

file_name = data.decode()
print("File Name:", file_name)

data, addr = server_socket.recvfrom(1024)
file_size = int(data.decode())
print("File Size:", file_size)

fl = open(file_name, 'wb')
data, addr = server_socket.recvfrom(1024)
i = 1
percent = 1024 * i / file_size * 100

while(percent < 100):
    print("current_size / total_size = ", 1024*i, "/", file_size, percent, "%")
    fl.write(data)
    data, addr = server_socket.recvfrom(1024)
    i = i + 1
    percent = 1024 * i / file_size * 100

fl.write(data)
print("current_size / total_size = ", file_size, "/", file_size, "100%")    
print("File Downloaded")
fl.close()
server_socket.close()