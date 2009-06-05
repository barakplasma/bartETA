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


def whichTags(need):
    global tags
    tags = xmldoc.getElementsByTagName(need)
    return tags

def whichStation(statN):
    station = statN
    stationInfo = taggedxml[station].childNodes
    return stationInfo 

def dataFields():
    global name, abbr, date, time, etaDests
    name = statInf[1].toxml()
    abbr = statInf[3].toxml()
    date = statInf[5].toxml()
    time = statInf[7].toxml()
    etaDests = statInf[9:]

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
        
def emailETAs(emailReq):
    #use this http://docs.python.org/library/email-examples.html#email-examples
    smtpuser = 'nxtBart@gmail.com'
    smtppass = 'thebartisawesome'#change this password!
    fromaddr = 'Service Account <nextTrain@gmail.com>'
    toaddrs = emailReq.split()
    bccaddrs = 'nextTrain+self@gmail.com'
    subject = "your next train from " + name
    dataFields()
    msg = ""
    msgAddon = ""
    msgAddon += name+abbr+date+time
    i = 0
    for childNodes in etaDests:
        msgAddon += etaDests[i].toxml()
        i = i + 1
    msg = msg+msgAddon
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls() 
    server.ehlo()
    server.login(smtpuser, smtppass)
    server.sendmail(fromaddr, toaddrs, msg)
    try:
        server.quit()
    except:
        pass
def userIn():
    iwant = (raw_input("station (ex. 'dbrk'): "))
    #Connor N. contributer
    statNum = ["12th", "16th","19th","24th","ashb", "balb","bayf", "cast", "civc", "cols", "colm", "conc", "daly", "dbrk", "dubl", "deln", "plza", "embr", "frmt", "ftvl", "glen", "hayw", "lafy", "lake", "mcar", "mlbr", "mont", "nbrk", "ncon", "orin", "pitt", "phil", "powl", "rich", "rock", "sbrn", "sfia", "sanl", "shay", "ssan", "ucty", "wcrk", "woak"]
    n = statNum.index(iwant)
    return n
def main():
    global taggedxml,statInf
    taggedxml = whichTags('station')
    statInf = whichStation(userIn()) #userIn() for testing
    displayETAs()
    emailETAs('barakplasma@gmail.com')
     
if __name__=="__main__":
    main()
