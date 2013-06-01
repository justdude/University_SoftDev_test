'''
server classes
@author: ivan
'''

import socket
import time
from threading import Thread 
#######################################################
def Receive():
    data=conn_receiver.recv(1024) 
    if data:
        print "Server recv DATA: "+data
#####################################################
receive=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
receive.bind(("127.0.0.1",82))
receive.listen(3)

send=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
send.bind(("127.0.0.1",81))
send.listen(3)
#######################################################
conn_sender, adr = send.accept()
print "Connected conn_sender", adr
conn_receiver, adr = receive.accept()
print "Connected conn_receiver", adr

#######################################################
Thread(target=Receive).start()

while True:
  conn_sender.send("Hello, userNAME")
  time.sleep(2)
  
#######################################################  
conn_sender.close()
conn_receiver.close()