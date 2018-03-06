#!/usr/bin/python

import sys

n_Hit, maxHits = 0, 0
prevPage, popularPage = None, None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Skip if not in key, value pair format
        continue

    # split input
    page, _ = data_mapped

    # check if new page, if new page, check if new max hits
    if prevPage and prevPage != page:
        if n_Hit > maxHits:
            maxHits = n_Hit
            popularPage = prevPage
        
        prevPage = page;
        n_Hit = 0

    # tally same page count
    prevPage = page
    n_Hit += 1

if prevPage != None:
    if n_Hit > maxHits:
        maxHits = n_Hit
        popularPage = prevPage

print "{0}\t{1}".format(popularPage, maxHits)