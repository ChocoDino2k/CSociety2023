import socket
from threading import Thread
import sys

games = []

class Game(Thread):
   def __init__(self, id, client):
      self.id = id
      self.isFull = 0
      self.clients = [client]
      self.data = ""
      Thread.__init__(self)
   def closeGame(self):
      self.clients[0].shutdown(socket.SHUT_RDWR)
      self.clients[0].close()
      self.clients[1].shutdown(socket.SHUT_RDWR)
      self.clients[1].close()

   def sendMessage(self, mes):
      self.clients[0].send(mes.encode())
      self.clients[1].send(mes.encode())
   def receiveData(self):
      d1 = self.clients[0].recv(10).decode()
      d2 = self.clients[1].recv(10).decode()
      print("From d1: {0}".format(d1))
      print("From d2: {0}".format(d2))
      if d1 == "quit" or d2 == "quit":
         self.data = "quit"
         print("Quitting the game")
         return
      if d1 == "e" and d2 != "e":
        self.data = d2
      elif d2 == "e" and d1 != "e":
        self.data = d1
      elif d1 != "e" and d2 != "e":
        self.data = d1
      print(self.data)

   def addClient(self, client):
      print("adding another client")
      self.clients.append(client)
      self.isFull = 1

   def run(self):
      try:
         while not self.isFull:
            continue
         print("received another client")
         #send initial start message
         self.sendMessage("start")
         #wait for both parties to acknowledge the start
         self.receiveData()
         self.data = "u(10,10)"
         while self.data != "quit":
            print("Sending data")
            self.sendMessage(self.data)
            print("Waiting for data")
            self.receiveData()
         self.closeGame()
         
      except KeyboardInterrupt:
         self.closeGame()
         sys.exit(1)
         

def startServer():
   host = "172.16.65.118"
   port = 8000 # arbitrary non-privileged port
   soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   print("Socket created")
   try:
      soc.bind((host, port))
   except:
      print("Bind failed. Error : " + str(sys.exc_info()))
      sys.exit()
   soc.listen(6) #6 at a time
   idCount = 0
   gameId = 0
   try:
     while True:
       conn, address = soc.accept()
       ip, port = str(address[0]), str(address[1])
       print("Connected with " + ip + ":" + port)
       #start thread
       idCount += 1
       gameId = (idCount - 1)//2
       if idCount % 2 == 1:
          games.append(Game(gameId, conn))
          games[gameId].start()
       else:
          games[gameId].addClient(conn)

   except KeyboardInterrupt:
     #print(e)
     print("Stopping server")
     #soc.shutdown(socket.SHUT_RDWR)
     for game in games:
        game.closeGame()
     soc.close()
     sys.exit()
#Execution starts here
startServer()