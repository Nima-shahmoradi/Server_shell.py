# Owner : Nima Shahmoradi 
# https://github.com/Nima-shahmoradi/Server_shell.py

from socket import *

ip = raw_input("Ip Server = ")
port = input("port server = ")

s=socket(AF_INET , SOCK_STREAM) # tcp connection
s.bind((ip,port))
s.listen(5)

print "Server Runing on port "+str(port)+'\n\n'

c , addr = s.accept()

print "Open Session "+str(addr)+'\n'

while True:

	shell = raw_input(c.recv(1024))

	if shell == None or shell == '' or shell == "\n":
		c.sendall('-')
		continue

	c.send(shell)
	
	data = c.recv(102343)

	print data

c.close()


