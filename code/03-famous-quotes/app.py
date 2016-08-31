#!/usr/bin/env python

import urllib
from bs4 import BeautifulSoup
url = 'https://litemind.com/best-famous-quotes'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")
for quote in soup.findAll('div',{'class':'wp_quotepage'}):
  text = quote.findChildren()[0].renderContents()
  author = quote.findChildren()[1].renderContents()
  print text, author
