#!/usr/bin/python


# Loop through input text to get item category and cost data
import sys

for line in sys.stdin:
    # delimit by tab
    data = line.strip().split("\t")
    # check log file has 6 items
    if len(data) == 6:
        # assign headers to each delimitted line
        date, time, store, item, cost, payment = data
        # output item category and cost
        print "{0}\t{1}".format(item, cost)

