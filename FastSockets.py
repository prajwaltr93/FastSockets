#!python

'''
module to create client and server sockets
Author--Prajwal T R
Date - 2/12/2018
'''

import socket

class Create():
    ''' Call this Class first to create a basic object'''
    def __init__(self,host=None):
        self.s =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        if (host==None):
            ByName = socket.gethostname()
            self.host = socket.gethostbyname(ByName)
        else:
            self.host = host
    def Server(self,port = 9999):
        self.s.bind((self.host,port))
    def Client(self,chost,port = 9999):
        self.s.connect((chost,port))
        self.conn = self.s
    def Listen(self,number):
        self.s.listen(number)
        self.conn,self.addr = self.s.accept()
    def Send(self,data):
        self.conn.send(data)
    def Recv(self,size):
        return self.s.recv(size)
    def Close(self):
        self.s.close()
