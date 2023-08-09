import socket

def ip():
	while True:
         print("enter website name:")
         add = input()
         ip = socket.gethostbyname(add)
         print(ip)
   
ip()