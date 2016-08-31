#!/usr/bin/env python

import urllib
from bs4 import BeautifulSoup

baseurl = 'http://localhost:8000'
url = baseurl + '/search/cpg'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
for link in soup.findAll('a',{'class':'hdrlnk'}):
  gigurl = baseurl + link['href']
  gig = urllib.urlopen(gigurl).read()
  gigsoup = BeautifulSoup(gig,'html.parser')
  title = gigsoup.find('span',{'id':'titletextonly'}).renderContents()
  print "TITLE:", title
  body = gigsoup.find('section',{'id':'postingbody'}).renderContents()
  print "BODY:", body
