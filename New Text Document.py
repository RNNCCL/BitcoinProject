import os
import binascii
import shutil
import stat
import io
import re
import urllib2
import urllib
import httplib
from urllib2 import Request, urlopen, URLError, HTTPError
def main():

	domin = "www.huobi.com"
	subdomin = "/staticmarket/detail.html"
 
	conn = httplib.HTTPConnection(domin)
	conn.putrequest('GET',subdomin)
	conn.putheader("User-Agent", "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)")
	conn.putheader("Accept", "*/*")
	conn.endheaders()
 
	result = conn.getresponse().read()
	print result
if __name__ == "__main__":
    main()
