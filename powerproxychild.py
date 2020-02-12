#!/usr/bin/env python

import urllib2, socket
from multiprocessing import Process, Pipe

class powerproxychild:

	proxyList = []
	testsite = ""
	begin = 0
	end = 0
	botnum = -1
	queue = 0
	showerrors = False

	def is_bad_proxy(self, pip, num):    
		try:        
		    proxy_handler = urllib2.ProxyHandler({'http': pip})        
		    opener = urllib2.build_opener(proxy_handler)
		    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
		    urllib2.install_opener(opener)        
		    req=urllib2.Request(str(self.testsite))  # change the url address here
		    sock=urllib2.urlopen(req)
		except urllib2.HTTPError, e:        
		    #print 'Error code: ', e.code
		    lasterror=e.code
		    return e.code
		except Exception, detail:
		    
			if self.showerror:
				print "[", self.botnum, "]", "testing:", num, "/", self.end," : ",pip,":",
				print "ERROR:", detail
		    return 1
		return 0
	
	def testProxies(self):
		print "[", self.botnum, "] STARTING from index: ", self.begin, " to index: ", self.end
		for i in range(self.begin, self.end):
			item = self.proxyList[i]
			
			if self.is_bad_proxy(item, i):
				self.begin = self.begin + 1
				self.begin = self.begin - 1
			else:
				print "\033[0;32m","WORKING", item, "\033[0;0m"
				#self.queue.send(["FOUND WORKING"])
				#self.queue.close()
				with open("working.txt", "a") as myfile:
					myfile.write(item + "\n")
		print "[", self.botnum, "] FINISHED"

	def __init__(self, botnum, begin, end, proxyList, sockettimeout, testsite, showerrors):
		self.proxyList = proxyList
		self.begin = begin
		self.end = end
		self.botnum = botnum
		self.testsite = testsite
		self.showerrors = showerrors
		socket.setdefaulttimeout(sockettimeout) # in seconds
		#self.queue = q
