import socket
import threading
import os
import sys

#takes in a socket to wait for second connection

#Game class that holds, sends, and receives data to the client
class Game:
    isFull = 0
    clients = []
    data = ""
    #will send the same response to both clients
    #TODO: send data to both clients
    def sendData():
        print("sending")
    #wait for both clients to send a response, then save it
    #TODO: wait for both clients and then set data
    def receiveData():
        print("receiving")
    #add a client to the clients list and set full
    #TODO: add locks, return status, and start state
    def addClient(client):
        print(f"adding client ${0}", client)



def send_response(client):
    text = "We received your connection "
    client.send(text.encode())


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 2000



s.bind( ("192.168.1.5", port) )
s.listen(5)
alive_clients = {}

try: 
    while True:
        client, address = s.accept()
        #stage = threading.Thread(target=staging, name="staging", args=(client))
        print(f"connection: {0}", address)
        #add the client to the list of alive_clients
        alive_clients[client.getpeername()[1]] = client
        send_response(client)
        #TODO: create a thread with the game state and add a client to it
except KeyboardInterrupt:
    print("closing")
    text = "Closing the server"

    for c in alive_clients:
        alive_clients[c].send(text.encode())
        alive_clients[c].close()

    s.close()
    sys.exit(0)

