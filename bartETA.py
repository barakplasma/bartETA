import urllib
import sys
import smtplib
from xml.dom import minidom
import pdb

address = 'http://bart.gov/dev/eta/bart_eta.xml'
xmldoc = minidom.parse(urllib.urlopen(address))

tags = []
station = 0
stationInfo = []
etaDests = []
name = []
abbr = []
date = []
time = []


#print xmldoc.toprettyxml()
def whichTags(need):
    tags = xmldoc.getElementsByTagName(need)
    #print tags[0].toxml()
def whichStation(statN):
    #pdb.set_trace()
    station = statN
    #print tags
    #print tags[station].toxml()
    stationInfo = tags[station].childNodes
    #print stationInfo
    
def dataFields():
    name = stationInfo[1].toxml()
    abbr = stationInfo[3].toxml()
    date = stationInfo[5].toxml()
    time = stationInfo[7].toxml()
    etaDests = stationInfo[9:]
    #cleanEta(3)
def cleanEta(a):
    for n in range(1,a):
        del etaDests[a]
def displayETAs():
    print name,abbr,date,time
    i = 0
    for childNodes in etaDests:
        print etaDests[i].toxml()
        i = i+1

def main():
    # the main code goes here
    whichTags('station')
    whichStation(13)
    dataFields()
    displayETAs()
 
if __name__=="__main__":
    main()