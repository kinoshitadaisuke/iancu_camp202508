#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/07/31 14:44:10 (UT+08:00) daisuke>
#

# data file
file_data = 'sample_00.data'

# initialisation of total price
total = 0

# opening file for reading
with open (file_data, 'r') as fh_in:
    # reading file line-by-line
    for line in fh_in:
        # if the first character of the line is '#', then skip
        if (line[0] == '#'):
            continue
        # splitting line
        (fruit, unitprice_str, quantity_str) = line.split ()
        # converting string into integer
        unitprice = int (unitprice_str)
        quantity  = int (quantity_str)
        # calculating subtotal
        subtotal = unitprice * quantity
        # adding subtotal to total
        total += subtotal

# printing result of calculation
print (f'total price : {total}')
