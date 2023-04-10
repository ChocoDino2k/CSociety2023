import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.184.94.6", 2000))
#s.send('Sup Server'.encode())
try: 
	while True:
		received = s.recv(128).decode()
		print(received)
		print()
		if (received == "Closing the server"):
			print("The server was closed")
			break
		elif (received == "waiting"):
			continue
		elif (received == "starting"):
			print("Another person connected")
			s.close()
		time.sleep(1)

except KeyboardInterrupt:
	s.close()

s.close()
