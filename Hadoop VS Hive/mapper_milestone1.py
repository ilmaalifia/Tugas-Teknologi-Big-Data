#!/home/bigdata/anaconda3/bin/python

import sys

for line in sys.stdin:
    row = line.strip().split('\t')
    date, time, city, product, value, payment = row

    if ('toys' in product.lower()) or ('consumer electronics' in product.lower()):
        print(product.strip(), '\t', value.strip())