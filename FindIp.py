import socket

def ip():
	while True:
         print("enter website name:")
         web = input()
         ip = socket.gethostbyname(web)
         print(ip)
   
ip()
