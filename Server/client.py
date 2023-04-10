import socket
import sys
def main():
   soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   host = "172.16.65.118"
   port = 8000
   try:
      soc.connect((host, port))
      #wait for start message
      mes = soc.recv(128).decode()
      print(mes)
      #acknowledge the start
      soc.send("u".encode())
      while mes != "end":
         mes = soc.recv(10).decode()
         print(mes)
         i = input()
         soc.send(i.encode())
         if (i == "quit"):
            soc.close()
            return
   except:
      print("Connection Error")
      sys.exit()
   print("Please enter 'quit' to exit")


main()