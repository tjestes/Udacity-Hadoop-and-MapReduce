#!/usr/bin/python

import sys

old_store = None
max_sale = 0

# Loop through data
# Loop through key, value data (store, sale)
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    (store, sale) = data_mapped
    sale = float(sale)

	# if new store, set max value
    if old_store and old_store != store:
        print old_store, "\t", max_sale
        old_store = store;
        max_sale = sale
    # if same store, check for new max value
    else:
    	old_store = store
        if sale > max_sale:
        	max_sale = sale

if old_store != None:
    print "{0}\t{1}".format(store, max_sale)