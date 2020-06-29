#!/home/bigdata/anaconda3/bin/python

import sys
import time

init_time_1 = time.strptime('09:01', '%H:%M')
final_time_1 = time.strptime('10:00', '%H:%M')
init_time_2 = time.strptime('10:01', '%H:%M')
final_time_2 = time.strptime('11:00', '%H:%M')

for line in sys.stdin:
    row = line.strip().split('\t')
    date, now_time, city, product, value, payment = row
    now_time = time.strptime(now_time.strip(), '%H:%M')

    if init_time_1 <= now_time and now_time <= final_time_1:
        print('09:01-10:00', '\t', 1)
    elif init_time_2 <= now_time and now_time <= final_time_2:
        print('10:01-11:00', '\t', 1)