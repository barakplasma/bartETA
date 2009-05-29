import getpass, imaplib

M = imaplib.IMAP4_SSL('imap.gmail.com', 993)
userName = "nxtBart"
pw = "thebartisawesome"
M.login(userName,pw)
print "logged in"
M.select()
typ, data = M.search(None, 'ALL')
print "printing msg's now"
for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    print 'Message %s\n%s\n' % (num, data[0][1])
M.close()
M.logout()
