#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    # check log file has 6 items
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(store, cost)

