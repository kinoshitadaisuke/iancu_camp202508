#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/08/04 11:16:46 (UT+08:00) daisuke>
#

# importing gzip module
import gzip

# importing sys module
import sys

# data file
file_data = 'table1.dat.gz'

# output file
file_output = 'co.data' 

# making an empty dictionary for storing data
dic_co = {}

# opening file for reading
with gzip.open (file_data, 'rb') as fh_in:
    # reading data line-by-line
    for line in fh_in:
        # extracting data from data file
        number_str = line[0:4]
        glon_str   = line[26:39]
        glat_str   = line[53:66]
        flag_str   = line[212:213]
        dnear_str  = line[214:226]
        dfar_str   = line[227:239]
        Mnear_str  = line[320:332]
        Mfar_str   = line[333:345]
        # converting strings into integer or float
        try:
            number = int (number_str)
            glon   = float (glon_str)
            glat   = float (glat_str)
            flag   = int (flag_str)
            dnear  = float (dnear_str)
            dfar   = float (dfar_str)
            Mnear  = float (Mnear_str)
            Mfar   = float (Mfar_str)
        except:
            sys.exit (0)
        # distance in kpc
        if (flag == 0):
            dist_kpc = dnear
            M_Msun = Mnear
        elif (flag == 1):
            dist_kpc = dfar
            M_Msun = Mfar
        else:
            sys.exit (0)
        # adding data to dictionary
        if not (number in dic_co):
            dic_co[number] = {}
        dic_co[number]['glon']     = glon
        dic_co[number]['glat']     = glat
        dic_co[number]['dist_kpc'] = dist_kpc
        dic_co[number]['M_Msun']   = M_Msun

# writing data into output file
with open (file_output, 'w') as fh_out:
    # writing header
    header = f'# cloud number, glon in deg, glat in deg, distance in kpc\n'
    fh_out.write (header)
    # writing data
    for number in sorted (dic_co.keys ()):
        record = f'{number:4d}' \
            + f' {dic_co[number]["glon"]:13.6f}' \
            + f' {dic_co[number]["glat"]:13.6f}' \
            + f' {dic_co[number]["dist_kpc"]:12.6f}' \
            + f' {dic_co[number]["M_Msun"]:12.3f}\n'
        fh_out.write (record)
