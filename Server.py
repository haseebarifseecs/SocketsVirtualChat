import socket
import threading as thread

class Server:
    #Specifying that our server will use IPv4 and TCP protocol
    conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #Creating an array to store each client connection info
    clientInfo = {}
    #Defining default constructor
    def __init__ (self):
        #binding the host ip address and port no with the connection
        self.conn.bind(('192.168.10.136',28960))
        #listening for incoming connection
        self.conn.listen(1)
    #handler method for each new thread
    def handler(self,clientConn,clientIP):
        #Sending the raw bytes of data to each new connection
        clientConn.send(bytes("""Welcome to the Chat Server.
                                 Inorder to change your name type /name/YourNewNickName
                                 Inorder to mute notifications type/sleep/TimetoMute
                                 Inorder to send a file type/send/Filepath Filename
                                 Enjoy your stay\n""",'utf-8'))
        #While there is data being received from any client forward it to all the connected clients
        while True:
            try:
                data = clientConn.recv(1024)
                print(str(data.decode('utf-8')))
            except Exception as e:
                data = 1
            for eachConnection in self.clientInfo:
                if eachConnection == clientConn:
                    continue
                if self.clientInfo[eachConnection] == 1:
                    try:
                        eachConnection.send(data)
                    except Exception as e:
                        continue
                        #self.clientInfo[eachConnection] = 0
                else:
                    pass
                    
            if not data:
                break
    def run(self):
        #For each new incoming connection we will create a new thread to allow multiple connections otherwise we can only handle one conn at a time
        while True:
            clientConn,clientIP = self.conn.accept()
            try:
                newThread = thread.Thread(target = self.handler,args=(clientConn,clientIP))
                newThread.daemon = True
                newThread.start()
            except Exception in thread as e:
                print('Exception occured')
    def close(self):
        self.conn.close()
cmd = input ('')
if cmd == 'start':
    print('[+] Listening For Incoming Connections [+]')
    server = Server()
    server.run()
else:
    server.close()

        
    
        
