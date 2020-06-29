#!/home/bigdata/anaconda3/bin/python

import sys

old_product = None
total_value = 0

for line in sys.stdin:
    row = line.split('\t')
    product, value = row
    value = float(value)

    if old_product and product != old_product:
        print(old_product, '\t', total_value)
        total_value = value
    else:
        total_value += value

    old_product = product

if old_product != None: 
    print(old_product, '\t', total_value)