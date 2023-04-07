import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.5", 2000))
#s.send('Sup Server'.encode())
try: 
	while True:
		received = s.recv(128).decode()
		if (received == "Closing the server"):
			print("The server was closed")
			break

except KeyboardInterrupt:
	s.close()

s.close()
