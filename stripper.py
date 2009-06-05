import os
os.system('grep "Subject: nxtTrain" currLastRequest.txt > currRequest.txt')
request = open('./currRequest.txt','r+')
manipulate = request.read()
print manipulate
use = manipulate[18:]
print use
os.system('python bartETA.py %s' % use)
request.close()
