import socket
import threading
import time
#socket is an ednpoint that recieves data and an endpoint sits in an IP

PORT = 5050
HEADER = 8
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

SERVER = socket.gethostbyname(socket.gethostname()) #instead of hardcoing the local IP
#we can use the inbuilt module to get the local IP

ADDR = (SERVER, PORT) #This a tupe and you can only bind a tuple


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#sock stream is for TCP 
#AF is address family and PF is protol family 
#inet is for internet 

#server.bind((SERVER, PORT))
#instead of the above line we use 
server.bind(ADDR)

def handle_client(conn, addr): #connection and address as arguments
  #this runs concurrently 
  print(f"[NEW CONNECTION] {addr} connected")

  connected = True
  while connected:
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if msg_length:
      msg_length = int(msg_length)
      msg = conn.recv(msg_length).decode(FORMAT)

      if msg == DISCONNECT_MESSAGE:
        connected = False


      print(f"[{addr}] {msg}")

  conn.close()


def start(): #starting the server, listening to connections and handling those connections
  server.listen()

  print(f"[LISTENING] Server is listening on {SERVER} ")

  while True:
    conn, addr = server.accept() #conn is the client socket and its a socket object
    #after this we can start a new thread that handles the client, handles all communications between client and server 
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    #refer to the threading for more info
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}") #we minus 1 to remove the main thread count
    print("Sending byte stream ....")
    msg_to_send = bytes("Welcom to the server!", FORMAT)
    conn.send(msg_to_send)
    conn.close()
print("[STARTING] Server is starting...")

start()