#!/usr/bin/env python

from powerproxychild import powerproxychild
import argparse
from multiprocessing import Process, Pipe

parser = argparse.ArgumentParser()
parser.add_argument("testsite", help="what website to test to proxy", default="www.reddit.com", nargs='?')
parser.add_argument("botnum", help="amount of bot subprocesses to use", default=2, type=int, nargs='?')
parser.add_argument("proxyfile", help="name of proxy text file", default="proxies.txt", nargs='?')
args = parser.parse_args()

print args;

f = open(args.proxyfile, 'r')
content = f.read()
content = content.split("\n")

pl = content

ppcList = []
ppcThreads = []

botWorkload = len(pl) / args.botnum

for i in range(0, args.botnum):
	#q = Pipe()
	t = Process(target=powerproxychild(i, botWorkload*i, botWorkload*(i+1), pl).testProxies)
	ppcList.append(powerproxychild(i, botWorkload*i, botWorkload*(i+1), pl))
	ppcThreads.append(t)
	t.start()
	#print(q.recv())
	print "[SYS] MANAGER: Created bot #", i

for i in range(0, len(ppcList)):
	ppcThreads[i].join();

