#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#TCP/IP server program that receive message from server. 


# In[ ]:


import socket
  
# take the server name and port name
host = 'local host'
port = 5000
  
# create a socket at server side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
  
# bind the socket with server
# and port number
s.bind(('', port))
  
# allow maximum 1 connection to
# the socket
s.listen(1)
  
# wait till a client accept
# connection
c, addr = s.accept()
  
# display client address
print("CONNECTION FROM:", str(addr))
  
# send message to the client after
# encoding into binary string
c.send(b"HELLO, How are you ?        Welcome to Akash hacking World")
 
msg = "Bye.............."
c.send(msg.encode())
  
# disconnect the server
c.close()

 





# In[ ]:


import socket
  
# take the server name and port name
  
host = 'local host'
port = 5000
  
# create a socket at client side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
  
# connect it to server and port
# number on local computer.
s.connect(('127.0.0.1', port))
  
# receive message string from
# server, at a time 1024 B
msg = s.recv(1024)
  
# repeat as long as message
# string are not empty
while msg:
    print('Received:' + msg.decode())
    msg = s.recv(1024)
 
# disconnect the client
s.close()


# In[ ]:




