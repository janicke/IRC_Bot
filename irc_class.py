
import socket
import sys
import time

class IRC:

    irc = socket.socket()
    def __init__(self):
        #Defines socket, AF_INET tells library to use  IPv4 and SOCK_STREAM tells library to use streamsockets
        self.irc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, channel, msg):
        #Function transfers data, send(bytes[flags]) is a function that sends data to a socket
        #PRIVMSG <msgtarget> :<message> .Sends <message> to <msgtarget>, which is usually a user or channel.
        #Defined in RFC 1459
        #bytes() function that returns bytestream, encoding UTF-8
        #channel is msgtarget and msg is message
        time.sleep(0.5)  #for UX
        self.irc.send(bytes("PRIVMSG "+channel+" "+msg+"\n", "ASCII"))

    def connect(self, server, port, channel, botname):
        #function to connect to server
        print("Connecting to: "+server)
        self.irc.connect((server, port))

        #Userauthentication process
        self.irc.send(bytes("USER " + botname + " " + botname + " " + botname + ": Whatup\n", "UTF-8"))
        self.irc.send(bytes("NICK "+botname+ "\n" , "UTF-8"))
        self.irc.send(bytes("JOIN " + channel + "\n" , "UTF-8"))

    def get_response(self):
        time.sleep(1)
        # Get the response
        resp = self.irc.recv(2040).decode("UTF-8")
        # to prevent unwanted timeout
        if resp.find('PING') != -1:
            self.irc.send(bytes('PONG ' + resp.split()[1] + '\r\n', "UTF-8"))

        return resp

