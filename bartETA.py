#!/usr/bin/env python
import urllib
import sys
import smtplib
from xml.dom import minidom
import pdb

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
    tags = xmldoc.getElementsByTagName(need)
    #print tags[0].toxml()
    return tags
def whichStation(statN):
    #pdb.set_trace()
    station = statN
    print taggedxml
    print taggedxml[station].toxml()
    stationInfo = taggedxml[station].childNodes
    #print stationInfo
    return stationInfo 
def dataFields():
    name = statInf[1].toxml()
    abbr = statInf[3].toxml()
    date = statInf[5].toxml()
    time = statInf[7].toxml()
    etaDests = stationInfo[9:]
    #cleanEta(3)
def cleanEta(a):
    for n in range(1,a):
        del etaDests[a]
def displayETAs():
    dataFields()
    print name,abbr,date,time
    i = 0
    for childNodes in etaDests:
        print etaDests[i].toxml()
        i = i+1

def main():
    # the main code goes here
    taggedxml = whichTags('station')
    statInf = whichStation(13)
    
    displayETAs()
 
if __name__=="__main__":
    main()
