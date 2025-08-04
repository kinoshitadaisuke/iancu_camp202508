#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/08/04 11:37:55 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# data file
file_data = 'co2.data'

# output file
file_output = 'clouds.png'

# making empty lists for storing data
list_x = []
list_y = []
list_z = []
list_M = []

# mass limit for visualisation
M_limit = 10**5

# opening file for reading
with open (file_data, 'r') as fh_in:
    # reading file line-by-line
    for line in fh_in:
        # skipping line if the line starts with '#'
        if (line[0] == '#'):
            continue
        # splitting line
        (number_str, x_str, y_str, z_str, M_str) = line.split ()
        # converting strings into integer and floats
        number = int (number_str)
        x_kpc  = float (x_str)
        y_kpc  = float (y_str)
        z_kpc  = float (z_str)
        M_Msun = float (M_str)
        # appending data to lists if the mass is greater than 10^5 solar mass
        if (M_Msun > M_limit):
            list_x.append (x_kpc)
            list_y.append (y_kpc)
            list_z.append (z_kpc)
            list_M.append (M_Msun)

# making Numpy arrays
array_x = numpy.array (list_x)
array_y = numpy.array (list_y)
array_z = numpy.array (list_z)
array_M = numpy.array (list_M)

# making a fig, canvas, and axes objects using object-oriented interface
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# making a plot using object-oriented interface
ax.plot (array_x, array_y, \
         linestyle='None', marker='.', markersize=1, color='b', \
         label='molecular clouds')
ax.set_xlabel ('Galactocentric $x$ [kpc]')
ax.set_ylabel ('Galactocentric $y$ [kpc]')
ax.set_xlim (-10.0, 10.0)
ax.set_ylim (-10.0, 10.0)
ax.set_aspect ('equal')
ax.legend ()
ax.grid ()

# making a PNG file
fig.savefig (file_output, dpi=150)
