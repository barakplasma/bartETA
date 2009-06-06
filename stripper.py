import os
from textwrap import fill
os.system('grep "Subject: nxtTrain" currLastRequest.txt > currRequest.txt')
os.system('grep "From: " currLastRequest.txt >> currRequest.txt')
request = open('./currRequest.txt','r+')
manipulate = request.readline()
#print manipulate
use = manipulate[18:]
#print use
reply = request.readline()
reply = reply.split('<')
#print reply
reply = reply[1]#.rstrip('>')
cutafter = reply.find('>')
reply = reply[:cutafter]
#print reply
use = " " + use + " " + reply
#use = use.replace('\n','')
#print fill(use)
#print use
command = "python bartETA.py" + use
command = fill(command)
#command += ' ' + use + ' ' + reply
print command
#os.system(command)#'python bartETA.py %s %s' % (use) (reply) ) # %s' % use)
os.system(command)
request.close()
