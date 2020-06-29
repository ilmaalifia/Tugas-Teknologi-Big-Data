#!/home/bigdata/anaconda3/bin/python

import sys

for line in sys.stdin:
    row = line.strip().split('\t')
    date, time, city, product, value, payment = row
    city = city.strip()

    if (city == 'Miami') or (city == 'Atlanta') or (city == 'San Francisco'):
        print(city.strip(), '\t', product.strip(), '\t', value.strip())