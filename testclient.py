import FastSockets as fs

'''
this is a test file to Demonstrate the use of FastSockets
'''
#Create a Object using Class Create()
obj = fs.Create()

host = input('enter host ip:')
#using Created object as Client
obj.Client(host,9999)
#to Demonstrate Recieving Data from Server
print(obj.Recv(1024).decode())
#closing client socket after use
obj.Close()
