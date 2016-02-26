from socket import *

def addNote():
    username = raw_input("Input Username:")
    username = username.lower()
    while (1):
        if username in usernames:
            username = raw_input("Username Already exists\nInput Username again:")
            username = username.lower()
        else:
            break
    usernames.append(username)   
    print " "
    notes = raw_input("Input your Note:")
    packet = str(choice)+str(username)+"=end="+ str(notes)
    #clientSocket.connect((serverIP,serverPort)) 
    clientSocket.send(packet)
    response = clientSocket.recv(1024)
    return response

def findNote():
    username = raw_input("Input Username:")
    username = username.lower()
    print " "
    packet = str(choice)+str(username)+"=end="
    #clientSocket.connect((serverIP,serverPort)) 
    clientSocket.send(packet)
    response = clientSocket.recv(1024)
    return response

def addNoteUNITTEST ():
    result = addNote()
    if result == "Record Added Successfully!!":
        print "UNIT TEST PASSED"
    else:
        print "UNIT TEST FAILDED"

def findNoteUNITTEST():
    result = findNote()
    if "NOTE:" in result or "No record found against Username" in result:
        print "UNIT TEST PASSED"
    else: 
        print "UNIT TEST FAILDED"

    
serverIP = "127.0.0.1"
serverPort = 10025
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP,serverPort))
usernames=[]
while (1):
    choice = raw_input("Choose from the following menu:\nPress 1 to add a note\nPress 2 to search a note\nYour Choice: ")
    print " "
    if (choice == "1"):
        output = addNote()
        ###########addNoteUNITTEST ()
        print "From Server:", output
    elif (choice == "2"):
        myoutput = findNote()
        ###########findNoteUNITTEST()
        print "From Server:", myoutput
    else:
        print "wrong input, enter again!"



clientSocket.close()
