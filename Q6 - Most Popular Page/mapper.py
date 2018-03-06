#!/usr/bin/python

import sys

for line in sys.stdin:
  data = line.replace('[','').replace(']','').replace('"','').replace('http://www.the-associates.co.uk','').split(' ')
  # check log file has 10 items
  if len(data) == 10:
    IP, ID, username, datetime, timezone, method, path, proto, status, size = data
    print "{0}\t{1}".format(IP, 1)