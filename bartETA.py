import urllib
import sys
import smtplib
from xml.dom import minidom

address = 'http://bart.gov/dev/eta/bart_eta.xml'
xmldoc = minidom.parse(urllib.urlopen(address))

#print xmldoc.toprettyxml()
tags = xmldoc.getElementsByTagName('station')
print tags[].toxml()