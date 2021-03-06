#!/home/bigdata/anaconda3/bin/python

import sys

old_time = None
total_count = 0

for line in sys.stdin:
    row = line.split('\t')
    time, count = row
    count = int(count)

    if old_time and time != old_time:
        print(old_time, '\t', total_count)
        total_count = count
    else:
        total_count += count

    old_time = time

if old_time != None: 
    print(old_time, '\t', total_count)


# CREATE TABLE IF NOT EXISTS purchases(dates string, times string, city string, product string, value float, payment string)
# ROW FORMAT DELIMITED 
# FIELDS TERMINATED BY '\t'
# STORED AS TEXTFILE 
# LOCATION '/purchases/';

# select product, sum(value)
# from purchases
# where product like '%Toys%'
# or product like '%Consumer Electronics%'
# group by product;

# create view city_sumvalue_product as
# select city, sum(value) as sum_value, product from purchases where city=='Miami' or city=='Atlanta' or city=='San Francisco' group by city, product;

# select temp1.city, temp1.sum_value, temp1.product from
# (city_sumvalue_product) as temp1 join
# (select city, max(sum_value) as sum_value from city_sumvalue_product group by city) as temp2
# on temp1.city==temp2.city and temp1.sum_value==temp2.sum_value;

# spark.sql("select temp1._c2, temp1.sum_value, temp1._c3 from (select _c2, sum(_c4) as sum_value, _c3 from purchases where _c2=='Miami' or _c2=='Atlanta' or _c2=='San Francisco' group by _c2, _c3) as temp1 join (select _c2, max(sum_value) as sum_value from (select _c2, sum(_c4) as sum_value, _c3 from purchases where _c2=='Miami' or _c2=='Atlanta' or _c2=='San Francisco' group by _c2, _c3) group by _c2) as temp2 on temp1._c2==temp2._c2 and temp1.sum_value==temp2.sum_value").show(5)

# create view bg5 as
# select case when cast(substr(times, 1, 2) as int)==9 and (cast(substr(times, 4, 2) as int) between 1 and 59) then '09:01-10:00'
# when cast(substr(times, 1, 2) as int)==10 and (cast(substr(times, 4, 2) as int)==0) then '09:01-10:00'
# when cast(substr(times, 1, 2) as int)==10 and (cast(substr(times, 4, 2) as int) between 1 and 59) then '10:01-11:00'
# when cast(substr(times, 1, 2) as int)==11 and (cast(substr(times, 4, 2) as int)==0) then '10:01-11:00'
# end as time, 1 as cnt
# from purchases;

# select time, sum(cnt) from bg5 group by time where time is not Null;

# spark.sql("select time, sum(cnt) from (select case when cast(substr(_c1, 1, 2) as int)==9 and (cast(substr(_c1, 4, 2) as int) between 1 and 59) then '09:01-10:00' when cast(substr(_c1, 1, 2) as int)==10 and (cast(substr(_c1, 4, 2) as int)==0) then '09:01-10:00' when cast(substr(_c1, 1, 2) as int)==10 and (cast(substr(_c1, 4, 2) as int) between 1 and 59) then '10:01-11:00' when cast(substr(_c1, 1, 2) as int)==11 and (cast(substr(_c1, 4, 2) as int)==0) then '10:01-11:00' end as time, 1 as cnt from purchases) where time is not Null group by time").show(5)