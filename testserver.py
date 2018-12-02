#!python

import FastSockets as fs
#Create a Object using Class Create()
obj = fs.Create()
port = 9999
#using Created object as Server
#to use a hostname of your choice set obj.host = 'your ip'
#then use obj.server method
obj.Server(port)

print('server initiated on host :',obj.host,'  ',port)

#usign listen(number) number = number of connections to accept
obj.Listen(1)
print('client connected to',obj.conn)
#using Send*(data) data shoould be encoded to send data to client
obj.Send('hiii'.encode())

obj.Close()
