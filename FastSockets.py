#!python

'''
module to create client and server sockets
Third-Party API
Author--Prajwal T R
Date - 2/12/2018
'''

import socket

class Create():
    ''' Call this Class first to create a basic object'''
    def __init__(self):
        self.s =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ByName = socket.gethostname()
        self.host = socket.gethostbyname(ByName)
    def Server(self,port = 9999):
        self.s.bind((self.host,port))
    def Client(self,host,port = 9999):
        self.s.connect((host,port))
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
