#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/08/04 11:35:58 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# data file
file_data = 'co.data'

# output file
file_output = 'co2.data'

# constants
R0_kpc    = 8.34
z0_kpc    = 0.025
theta_rad = numpy.arcsin (z0_kpc / R0_kpc)
sin_theta = z0_kpc / R0_kpc
cos_theta = numpy.sqrt (1.0 - sin_theta**2)

# making an empty dictionary for storing data
dic_clouds = {}

# opening file for reading
with open (file_data, 'r') as fh_in:
    # reading file line-by-line
    for line in fh_in:
        # skipping if the line starts with '#'
        if (line[0] == '#'):
            continue
        # splitting line
        (number_str, glon_deg_str, glat_deg_str, dist_kpc_str, M_Msun_str) \
            = line.split ()
        # converting strings into integer and floats
        number   = int (number_str)
        glon_deg = float (glon_deg_str)
        glat_deg = float (glat_deg_str)
        dist_kpc = float (dist_kpc_str)
        M_Msun   = float (M_Msun_str)
        # converting units
        glon_rad = glon_deg / 180.0 * numpy.pi
        glat_rad = glat_deg / 180.0 * numpy.pi
        # calculation of galactocentric coordinates
        x_gal_kpc = R0_kpc * cos_theta \
            - dist_kpc * (numpy.cos (glon_rad) * numpy.cos (glat_rad) \
                          * cos_theta \
                          + numpy.sin (glat_rad) * sin_theta)
        y_gal_kpc = -1.0 * dist_kpc * numpy.sin (glon_rad) * numpy.cos (glat_rad)
        z_gal_kpc = R0_kpc * sin_theta \
            - dist_kpc * (numpy.cos (glon_rad) * numpy.cos (glat_rad) \
                          * sin_theta - numpy.sin (glat_rad) * cos_theta)
        # adding data to dictionary
        if not (number in dic_clouds):
            dic_clouds[number] = {}
        dic_clouds[number]['x_gal']  = x_gal_kpc
        dic_clouds[number]['y_gal']  = y_gal_kpc
        dic_clouds[number]['z_gal']  = z_gal_kpc
        dic_clouds[number]['M_Msun'] = M_Msun
        
# writing data to new file
with open (file_output, 'w') as fh_out:
    header = f'# molecular cloud number,' \
        + f' x_gal [kpc], y_gal [kpc], z_gal [kpc], M [Msun]\n'
    fh_out.write (header)
    for number in (sorted (dic_clouds.keys ())):
        record = f'{number:4d}  {dic_clouds[number]["x_gal"]:10.6f}' \
            + f'  {dic_clouds[number]["y_gal"]:10.6f}' \
            + f'  {dic_clouds[number]["z_gal"]:10.6f}' \
            + f'  {dic_clouds[number]["M_Msun"]:12.3f}\n'
        fh_out.write (record)
