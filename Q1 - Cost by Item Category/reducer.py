#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None

# Loop through data
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    # Skip if not in key, value pair format
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped

    # check if new key
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesTotal
        oldKey = thisKey;
        salesTotal = 0

    # total value for same key
    oldKey = thisKey
    salesTotal += float(thisSale)

if oldKey != None:
    print "{0}\t{1}".format(oldkey, salesTotal)

