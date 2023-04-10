import socket
from threading import Thread
import os
import sys

#takes in a socket to wait for second connection

#Game class that holds, sends, and receives data to the client
class Game(Thread):
  def sendData(self):
    print("sending")
    self.clients[0].send(self.lastCommand.encode())
    self.clients[1].send(self.lastCommand.encode())
    #wait for both clients to send a response, then save it
    #TODO: wait for both clients and then set data
  def receiveData(self):
    print("receiving")
    d1 = self.clients[0].recv(1024)
    d2 = self.clients[1].recv(1024)
    #no new response from first client
    if d1 == "none" and d2 != "none":
        self.lastCommand = d2
    elif d2 == "none" and d1 != "none":
        self.lastCommand = d1
    elif self.lastCommand == "":
        self.lastCommand = "up"

  def __init__(self, client):
    self.clients = [client]
    self.data = ""
    self.isFull = 0
    self.lastCommand = ""
    self.lastClientUsed = 0
    Thread.__init__(self)

  def run(self):
    print(self.isFull)
    try:
      while not self.isFull:
        text = "waiting"
        self.clients[0].send(text.encode())
      self.lastCommand = "starting"
      sendData()
      while True:
        receiveData()
        sendData()
    except Exception as e:
      print(e)
      print("Exception in game thread")
      return 1
    #will send the same response to both clients
    #TODO: send data to both clients

    #add a client to the clients list and set full
    #TODO: add locks, return status, and start state
  def addClient(self, client):
    print(f"adding client {0}", client)
    self.clients.append(client)
    self.isFull = 1



def send_response(client):
    text = "We received your connection "
    client.send(text.encode())


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 2000



s.bind( ("10.184.94.6", port) ) #192.168.1.5
s.listen(5)
alive_clients = {}
games = []
try: 
    while True:
        client, address = s.accept()
        print(f"connection: {0}", address)
        print(f"client: {0}", client)
        #add the client to the list of alive_clients
        alive_clients[client.getpeername()[1]] = client
        #send_response(client)
        makeNewGame = 1
	#find a game with an open slot
        for game in games:
            if not game.isFull:
                game.addClient(client)
                makeNewGame = 0
                break
        if makeNewGame:
            print("Making new game\n")
            game = Game(client)
            #game = threading.Thread(target=Game, name = "snake game", args=(client,)).start()
            games.append(game)
            game.start()
            print(game)
	
except KeyboardInterrupt:
    print("closing")
    text = "Closing the server"

    for c in alive_clients:
        alive_clients[c].send(text.encode())
        alive_clients[c].close()

    s.close()
    sys.exit(0)

