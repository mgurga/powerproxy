#!/usr/bin/env python

import urllib2, socket

f = open('proxies.txt', 'r')
content = f.read()
content = content.split("\n")

socket.setdefaulttimeout(10)

proxyList = content

lasterror=""
curnum = 0

def is_bad_proxy(pip):    
    try:        
        proxy_handler = urllib2.ProxyHandler({'http': pip})        
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib2.install_opener(opener)        
        req=urllib2.Request('http://www.reddit.com')  # change the url address here
        sock=urllib2.urlopen(req)
    except urllib2.HTTPError, e:        
        #print 'Error code: ', e.code
        lasterror=e.code
        return e.code
    except Exception, detail:
        print "ERROR:", detail
	print "";
        return 1
    return 0


for item in proxyList:
    curnum=curnum+1
    print "testing number:", curnum, "/", len(proxyList)," : ",item,":",lasterror,
    if is_bad_proxy(item):
        curnum = curnum + 1
        curnum = curnum - 1
    else:
        print "WORKING", item
	print "WORKING", item
	print "WORKING", item

