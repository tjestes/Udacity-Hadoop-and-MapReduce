#!/usr/bin/python

import sys

salesTotal = 0
n_sales = 0

# Loop through data
# Data will be inputted in key, value pairs
# Store will be the key
# Cost will be value
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    store, sales = data_mapped

	# if new store,  reset count
    if old_store and old_store != store:
        print old_store, "\t", max_sale
        old_store = store;
        n_sale = 0
    # if same store, check for new max value
    else:
    	old_store = store
        n_sale += 1

if old_store != None:
    print "{0}\t{1}".format(store, max_sale)