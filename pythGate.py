import imaplib
import os
#do something with this http://www.doughellmann.com/PyMOTW/imaplib/

M = imaplib.IMAP4_SSL('imap.gmail.com', 993)

userName = "nxtBart"
pw = "thebartisawesome"

M.login(userName,pw)
print "logged in"




M.select()
typ, data = M.search(None, 'ALL')
allmsgs = ""





for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    print 'Message %s\n%s\n' % (num, data[0][1])
    allmsgs += 'Message %s\n%s\n' % (num, data[0][1])
#print allmsgs





txtmsgs = open('./txtmsgs.txt','w')
txtmsgs.write(allmsgs)
#txtmsgs.read()
txtmsgs.close()
os.system("cp currLastRequest.txt 2ndrequest.txt")
os.system("tail -28 txtmsgs.txt > currLastRequest.txt")
#if new msg
os.system("diff -q currLastRequest.txt 2ndrequest.txt >> diffTrue.txt")
difference = open('./diffTrue.txt','r')
crazy = difference.read()
isdiff = ""
#if (crazy is equal to string diff)
if(!(crazy == isdiff))
    os.system("python stripper.py")
#run the prog
#run stripper.py

M.close()
M.logout()
