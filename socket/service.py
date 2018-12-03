"""
hostname,port:
make url usingport, hostname
need to wait for client request.
once it got the request, it has to accept that and process the request send response back
"""
import socket
hostname = socket.gethostname()
port=8889
try:
	s=secoket.socket()
	s.bind((hostname,port))
	while True:
		s.listen(200)
		print "serivce running in %s:%s"%(hostname,port)
		print "wait for the client request"
		clientsocket, cleint,info = s.accept()
		clientsocket.send("hello firefox how are you?")
		req_data=clientsocket.recv(10)
		try:
			resp = "EVEN" if int(req_data)%2==0 else "ODD"
		cleintsocket.send(resp)
s.close()
