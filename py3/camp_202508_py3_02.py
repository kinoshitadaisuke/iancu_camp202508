#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/07/31 14:51:20 (UT+08:00) daisuke>
#

# importing urllib module
import urllib.request

# URL of data file
url_data = 'https://s3b.astro.ncu.edu.tw/camp_202508/data/sample_01.data'

# output file name
file_output = 'sample_01.data'

# downloading data file
with urllib.request.urlopen (url_data) as fh_in:
    # reading data
    data_raw = fh_in.read ()
    # converting data to UTF-8 string
    data_utf8 = data_raw.decode ('utf-8')
    
# opening file for writing
with open (file_output, 'w') as fh_out:
    # writing data
    fh_out.write (data_utf8)
