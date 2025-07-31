#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/07/31 15:30:46 (UT+08:00) daisuke>
#

# importing math module
import math

# data file
file_data = 'sample_01.data'

# making an empty dictionary for storing data
dic_star = {}

# opening file for reading
with open (file_data, 'r') as fh_in:
    # reading data file line-by-line
    for line in fh_in:
        # skipping line if the line starts with '#'
        if (line[0] == '#'):
            continue
        # splitting line
        (star, mag_V_str, colour_BV_str, parallax_arcsec_str) = line.split ()
        # converting string into float
        mag_V           = float (mag_V_str)
        colour_BV       = float (colour_BV_str)
        parallax_arcsec = float (parallax_arcsec_str)
        # calculation of distance in parsec
        dist_pc = 1.0 / parallax_arcsec
        # calculation of absolute magnitude
        absmag_V = mag_V - 5.0 * math.log10 (dist_pc) + 5.0
        # adding data to dictionary
        if not (star in dic_star):
            dic_star[star] = {}
        dic_star[star]['mag_V']           = mag_V
        dic_star[star]['colour_BV']       = colour_BV
        dic_star[star]['parallax_arcsec'] = parallax_arcsec
        dic_star[star]['dist_pc']         = dist_pc
        dic_star[star]['absmag_V']        = absmag_V

# sorting dictionary by value and printing values
print (f'{"Name":16s}  {"Vmag":5s}  {"B-V":5s}  {"dist [pc]":9s}  {"absmag":6s}')
for star in sorted (dic_star.items (), key=lambda x: x[1]['absmag_V']):
    print (f'{star[0]:16s}  {star[1]["mag_V"]:+5.2f}',
           f' {star[1]["colour_BV"]:+5.2f}',
           f' {star[1]["dist_pc"]:9.1f}  {star[1]["absmag_V"]:+6.2f}')
