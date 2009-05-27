#!/usr/bin/env python
import urllib
import sys
import smtplib
from xml.dom import minidom
import pdb
import smtplib
from email.mime.text import MIMEText

address = 'http://bart.gov/dev/eta/bart_eta.xml'
xmldoc = minidom.parse(urllib.urlopen(address))

"""
tags = []
station = 0
stationInfo = []
etaDests = []
name = []
abbr = []
date = []
time = []
"""

#print xmldoc.toprettyxml()
def whichTags(need):
    global tags
    tags = xmldoc.getElementsByTagName(need)
    #print tags[0].toxml()
    return tags
def whichStation(statN):
    #pdb.set_trace()
    station = statN
    #print taggedxml
    #print taggedxml[station].toxml()
    stationInfo = taggedxml[station].childNodes
    #print stationInfo
    return stationInfo 
def dataFields():
    global name, abbr, date, time, etaDests
    name = statInf[1].toxml()
    abbr = statInf[3].toxml()
    date = statInf[5].toxml()
    time = statInf[7].toxml()
    etaDests = statInf[9:]
    #cleanEta(3)
def cleanEta(a):
    for n in range(1,a):
        del etaDests[a]
def displayETAs():
    dataFields()
    print name
    print abbr
    print date
    print time
    i = 0
    for childNodes in etaDests:
        print etaDests[i].toxml()
        i = i+1
        
def emailETAs():
    smtpuser = 'nxtBart@gmail.com'
    smtppass = 'thebartisawesome'
    fromaddr = 'Service Account <nextTrain@gmail.com>'
    toaddrs = 'barakplasma@gmail.com'.split()
    bccaddrs = 'nextTrain+self@gmail.com'
    subject = ("your next train from ",name+" "+abbr)
    msg = ("")
    #dataFields()
    msg += name+abbr+date+time
    msgAddon = ""
    i = 0
    for childNodes in etaDests:
        msgAddon += etaDests[i].toxml()
        i = i + 1
    msg = msg+msgAddon
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.set_debuglevel(1)
    #
    # Start the conversation with EHLO
    #
    server.ehlo()
    #
    # Request STARTTLS
    #
    server.starttls() 
    #
    # And say EHLO again
    #
    server.ehlo()
    #
    # Login to the server with SMTP AUTH now that were TLSd and client identified #
    server.login(smtpuser, smtppass)
    #
    # Finally, send the mail!
    #
    server.sendmail(fromaddr, toaddrs, msg)
    try:
        server.quit()
    except:
        pass
    """
    
    fp = open(textfile, 'rb')
    msg = MIMEText(fp.read())
    fp.close()
    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = 'The contents of %s' % textfile
    msg['From'] = me
    msg['To'] = you
    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP()
    s.sendmail(me, [you], msg.as_string())
    s.quit()
    """
def userIn():
    #print list of stations(fxn to convert 4 letter to station) 
    iwant = (raw_input("station (ex. 'dbrk'): "))
    #Connor N. contributer
    statNum = ["12th", "16th","19th","24th","ashb", "balb","bayf", "cast", "civc", "cols", "colm", "conc", "daly", "dbrk", "dubl", "deln", "plza", "embr", "frmt", "ftvl", "glen", "hayw", "lafy", "lake", "mcar", "mlbr", "mont", "nbrk", "ncon", "orin", "pitt", "phil", "powl", "rich", "rock", "sbrn", "sfia", "sanl", "shay", "ssan", "ucty", "wcrk", "woak"]
    n = statNum.index(iwant)
    return n
def main():
    """
    Here is how it works:
    Send an email to bart@barakplasma.dyn-o-saur.com
    with a subject line "nextBart dbrk"
    server recieves email
        email to a gmail account
        gmail account only forwards properly formatted emails
        postfix recieves emails
            http://flurdy.com/docs/postfix/
        
    uses python smtplib to parse email subject line
    redirect subject line argument "dbrk"
    to python script as follows:
    bartETA.py dbrk
    this calls previous script
    to send text from method displayETA()
    as email to the email sender
    """
    # the main code goes here
    global taggedxml,statInf
    taggedxml = whichTags('station')
    statInf = whichStation(userIn()) #userIn() for testing
    displayETAs()
    emailETAs()
     
if __name__=="__main__":
    main()
