# client.py  
import socket
import select
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()                           

port = 9999
s.connect((host, port))
cnt = 0 

while True:  

     sockets_list = [sys.stdin, s]

     read_sockets, write_socket, error_socket = select.select(sockets_list,[],[])

     for socks in read_sockets:
        if socks == s:
                                     
           data = socks.recv(2048)
           print data  
        else :                                  
           data = sys.stdin.readline()
           s.send(data)
           sys.stdout.write(data)
           sys.stdout.flush()

s.close()

