#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/08/01 12:08:10 (UT+08:00) daisuke>
#

# importing urllib module
import urllib.request

# URL of data file
url_data = 'https://cdsarc.cds.unistra.fr/ftp/J/ApJ/834/57/table1.dat.gz'

# output file name
file_output = 'table1.dat.gz'

# downloading data file
with urllib.request.urlopen (url_data) as fh_in:
    # reading data
    data_raw = fh_in.read ()
    
# opening file for writing
with open (file_output, 'wb') as fh_out:
    # writing data
    fh_out.write (data_raw)
