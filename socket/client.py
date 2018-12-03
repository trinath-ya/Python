import socket
hostname=
port=
s.socket(socket)
s.connect((hostname,port))
ack = s.recv(1024)
print "acknowledgemnt",ack
data = raw_input("enter number")
s.send(data)
resp = s.recv(10)
print "response: ",resp