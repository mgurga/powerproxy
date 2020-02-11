#!/usr/bin/env python3

import os
from multiping import multi_ping
from socket import socket
import urllib.request, urllib.error

f = open('proxies.txt', 'r')
content = f.read()
content = content.split("\n")

socket.setdefaulttimeout(180)

proxyList = content

def is_bad_proxy(pip):    
    try:        
        proxy_handler = urllib.request.ProxyHandler({'http': pip})        
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)        
        req=urllib.request('http://www.google.com')  # change the url address here
        sock=urllib.request.urlopen(req)
    except urllib.error.HTTPError as e: 
        print ('Error code: ' + e.code)
        return e.code
    except Exception as detail:

        print("ERROR:" + str(detail))
        return 1
    return 0

for item in proxyList:
    if is_bad_proxy(item):
        print("Bad Proxy" + item)
    else:
        print(item + "is working")

f.close()