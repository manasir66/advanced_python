import socket

HEADER = 8
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER, PORT))

def send(msg):
  pass



full_msg = "" #this so that we can maintain a small buffer size and append data 

while True:
  msg_to_get = client.recv(HEADER)
  if len(msg_to_get) <= 0:
    break
  full_msg += msg_to_get.decode(FORMAT)

print(full_msg)

