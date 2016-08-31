#!/usr/bin/env python

import urllib
import re
from cookielib import CookieJar # store cookies and logged-in info
import urllib2


# print html
html = urllib.urlopen("http://jshawl.com/python-playground").read()
print html

# download an image
urllib.urlretrieve("http://jshawl.com/python-playground/python.gif","python.gif")

# extract email addresses
print re.findall('[\w]+@[\w.]+', html)

# log in to a website
cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
formValues = {
  "username":"user",
  "password":"pass"
}
data = urllib.urlencode(formValues)
response = opener.open("http://jshawl.com/python-playground/login.php",data)
print response.read()

secure = opener.open("http://jshawl.com/python-playground/protected2.php")
print secure.read()
