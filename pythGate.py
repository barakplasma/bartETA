import imaplib
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





txtmsgs = open('./txtmsgs.txt','r+')
txtmsgs.write(allmsgs)
txtmsgs.read()
txtmsgs.close()




M.close()
M.logout()
