#! /bin/python

import urllib2
from bs4 import BeautifulSoup


def fun1():
	request = urllib2.Request("http://blog.marsw.tw")
	response = urllib2.urlopen(request)
	html = response.read()

	soup = BeautifulSoup(''.join(html), "lxml")

	for i in soup.find_all('a', href=True):
		print 

if __name__ == "__main__":
	fun1()