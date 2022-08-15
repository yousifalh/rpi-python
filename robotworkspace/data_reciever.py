import atexit
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 6060))
atexit.register(s.close)

with open("wheel_average_time.txt", 'w') as file:

    while True:
        message = s.recv(4096)
        
        file.write(message)




