#Client side
import socket
import threading
import sys
import re as regex
import time
import os
import ftplib as ftp
import random
class Client:
    #Creating TCP socket over IPv4
    socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    message = ''
    #Variables for the implemented logic for snoozing out the notifications
    snooze = False
    timer = 0
    blockUser = ''
    ftpIP = ''

        
        
    def sendMsg(self,name):
        while True:
           message = input("")
           #Stands true if there is any command in the input shell
           if '/' in message:
               pattern = '\/(.*?)\/'
               result = regex.findall(pattern,message)
               cmd = ''.join(result)
               rem = message[len(cmd)+2:]
               #Handles rename cmd
               if cmd == 'name':
                   self.socket.send(bytes(name + ' has renamed to ' + rem,'utf-8'))
                   name = rem
               #Handles Quit cmd
               elif cmd == 'quit':
                   self.socket.send(bytes(name + ' has left the chat','utf-8'))
                   self.socket.close()
                   break
               #Initializes logic for snoozing out the variables
               elif cmd == 'sleep':
                   self.timer = str(rem)
                   self.socket.send(bytes(name + ' snoozed the notifications for ' + self.timer + ' seconds.','utf-8'))
                   self.snooze = True
                #Initializes logic for sending file over FTP
               elif cmd == 'send':
                   file_data  = rem.split()
                   file_path = file_data[0]
                   file_name = file_data[1]
                   self.socket.send(bytes('[+] ' + name + ' is transferring a file named ' + file_name,'utf-8'))
                   time.sleep(1)
                   file = open(file_path,'rb')
                   try:
                       ftpcon = ftp.FTP(self.ftpIP)
                       ftpcon.login('ftpusername','ftppassword')
                       ftpcon.storbinary('STOR ' + '/' +file_name,file)
                       print('[+] File transferred sucessfully')        
                       ftpcon.close()
                       self.socket.send(bytes('DONE','utf-8'))
                       self.socket.send(bytes(file_name,'utf-8'))
                   except Exception as e:
                       print('[+] FTP server timeout')
               elif cmd == 'blacklist':
                   self.blockUser = rem
               elif cmd == 'unblock':
                   self.blockUser = ''
                   print('[+] ' + rem + ' has blacklisted successfuly.')
                  
                   
                   
           #Else if no cmd just forward the input message stream
           else:
               self.socket.send(bytes(name + ': ' + message,'utf-8'))
     #Main constructor to connect with the server          
    def __init__(self,serverIP,port,name,ftpip):
        self.ftpIP = ftpip
        self.socket.connect((address,port))
        self.socket.send(bytes(name + ' has joined the chat.','utf-8'))
        clientThread = threading.Thread(target=self.sendMsg,args=(name,))
        clientThread.daemon = True
        clientThread.start()
       #Main thread to handle snoozing logic and FTP download logic
        while True:
            if self.snooze == True:
                for i in range(int(self.timer),0,-1):
                    os.system('cls')
                    print('Notification Snoozed for ' + str(i) + ' seconds')
                    time.sleep(1)
                os.system('cls')
                self.snooze = False
            else:
                try:
                    data = self.socket.recv(1024)
                    info = str(data.decode('utf-8'))
                    if ':' not in info:
                        print(info)
                    if info == 'DONE':
                        print("[+] Please hold for a moment. Downloading file")
                        filename = str(self.socket.recv(1024).decode('utf-8'))
                        file = open(filename,'wb')
                        time.sleep(random.randint(1,5))
                        ftpcon = ftp.FTP(self.ftpIP)
                        ftpcon.login('ftpusername','ftppassword')
                        ftpcon.retrbinary('RETR ' + '/' +filename,file)
                        ftpcon.close()
                        file.close()
                        print("[+] File downloaded successfully.")
                        print("[+]Opening downloaded file..")
                        os.startfile(filename)
                    
                        

                    else:
                        if self.blockUser != '' and self.blockUser in info:
                            if 'renamed' in info:
                                self.blockUser = info[info.find('to')+3:]
                                continue
                            else:
                                continue
                    
                        else:
                            print('\n')
                            print(info)
                            print('Type Here:>>')
                    
                    
                except Exception as e:
                    data = 1
                    break
                if not data:
                    break

name = sys.argv[2]
serverIP = sys.argv[4]
port = sys.argv[6]
ftpIP = sys.argv[8]
client = Client(name,serverIP,port,ftpIP)
