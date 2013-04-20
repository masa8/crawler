from bs4 import BeautifulSoup as bs
import urllib2 
import urlparse
from urllib import urlretrieve
import os
import sys

site="http://en.wikipedia.org/wiki/Pune"
hdr= {'User-Agent': 'Mozilla/5.0'}
outfolder="/home/mayank/Desktop/test"
req = urllib2.Request(site,headers=hdr)
page = urllib2.urlopen(req)
soup =bs(page)
tag_image=soup.findAll("img")
for image in tag_image:
	print "Image: %(src)s" % image
	filename = image["src"].split("/")[-1]
	outpath = os.path.join(outfolder, filename)
	urlretrieve('http:'+image["src"], outpath)
