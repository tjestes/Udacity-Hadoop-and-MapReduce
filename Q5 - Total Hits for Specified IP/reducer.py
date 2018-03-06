#!/usr/bin/python

n_count = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    # Skip if not in key, value pair format
    if len(data_mapped) != 2:
      continue
      
    # split input
    _IP, _ = data_mapped
    
    # count only 10.99.99.186 IP hits
    if _IP == '10.99.99.186':
      IP = '10.99.99.186'
      n_count += 1    

print "{0}\t{1}".format(IP, n_count)