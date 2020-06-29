#!/home/bigdata/anaconda3/bin/python

import sys

old_product = None
old_city = None
total_value = 0
temp = []

for line in sys.stdin:
    row = line.split('\t')
    city, product, value = row
    value = float(value)

    if old_product and ((city != old_city) or (city == old_city and product != old_product)):
        temp.append(old_city + '\t' + old_product + '\t' + str(total_value))
        total_value = value
    else:
        total_value += value

    old_product = product
    old_city = city

if old_product != None: 
    temp.append(old_city + '\t' + old_product + '\t' + str(total_value))

old_city, max_product, max_value = temp[0].strip().split('\t')
max_value = float(max_value)
for line in temp[1:]:
    row = line.strip().split('\t')
    city, product, value = row
    value = float(value)
    if old_city and city != old_city:
        print(old_city, '\t', max_value, '\t', max_product)
        max_value = value
        max_product = product
    else:
        if max_value < value:
            max_value = value
            max_product = product
    
    old_city = city

if old_city != None:
    print(old_city, '\t', max_value, '\t', max_product)