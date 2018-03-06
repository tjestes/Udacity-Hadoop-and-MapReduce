#!/usr/bin/python

n_count = 0
previous_page = None

for line in sys.stdin.readlines():
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Skip if not in key, value pair format
        continue
    
    # split input
    page, _ = data_mapped

    # begin new count when new page registers
    if previous_page and previous_page != page:
        print page, "\t", _
        previous_page = page;
        n_count = 0
    
    # tally count when same page
    previous_page = page
    n_count += 1

if previous_page != None:
    print "{0}\t{1}".format(previous_page, n_count)