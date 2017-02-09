import socket
import sys

#create file
def createFile():
    with open("file_object.txt", 'w') as fileContent:
        fileContent.write('This is just cray cray\n')
        fileContent.close()

#read file
def readFile():
    with open('file_object.txt', 'r') as fileContent:
        content = fileContent.read()
        if content is None:
            fileContent.close()
    return content

#send the file data
def sendData(sock, dest):
    data = readFile()
    sock.sendto(bytes(data, 'UTF-8'), dest)

#setup socket
def setupUDPSocket():
    #create udp socket
    _socket = socket.socket(socket.AF_INET, #internet
                            socket.SOCK_DGRAM) # UDP
    #forceibly bind to port in use
    _socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    return _socket

#main
if __name__=='__main__':
    #destination address and port
    package_destination = ("192.168.0.67", 4001)
    #create udp socket
    sock = setupUDPSocket()
    #create a file to read
    createFile()
    #read the file
    readFile()
    #send file content over udp
    sendData(sock, package_destination)


