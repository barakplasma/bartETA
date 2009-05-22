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
    print name,abbr,date,time
    i = 0
    for childNodes in etaDests:
        print etaDests[i].toxml()
        i = i+1
def userIn():
    #print list of stations(fxn to convert 4 letter to station) 
    iwant = (raw_input("station (ex. 'dbrk'): "))
    #Connor N. contributer
    statNum= ["12th","16th","19th","24th","ashb","balb","bayf","cast","civc","cols","colm","","16th","16th","16th","16th","16th","16th","16th","16th","16th","16th","16th","16th","16th","16th","16th","16th","16th","16th","16th","16th","16th","16th","16th","16th","16th","16th","16th","16th","16th","16th","16th","16th"]
    n = statNum.index(iwant)
    return n
def main():
    # the main code goes here
    global taggedxml,statInf
 
   
    taggedxml = whichTags('station')
    statInf = whichStation(userIn())
    displayETAs()
     
if __name__=="__main__":
    main()
