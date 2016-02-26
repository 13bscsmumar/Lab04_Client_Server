from socket import *

def searchByName():
    if name in storage:
        index = storage.index(name)
        note = storage[index+1]
        connectionSocket.send("NOTE:\n"+name+": "+ note) 
    else:
        connectionSocket.send("No record found against Username"+name)

def addNote():
    note = packet[packet.index("=end=")+5:len(packet)]
    storage.append(name)
    storage.append(note)
    connectionSocket.send("Record Added Successfully!!") 
    
serverPort = 10025
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('127.0.0.1',serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
connectionSocket, addr = serverSocket.accept() 

storage=[]
while 1:
    packet = connectionSocket.recv(1024)
    choice = packet[:1]
    name = packet[1:packet.index("=end=")]
    if choice =="1":
        addNote()
    elif choice =="2":
        searchByName()
