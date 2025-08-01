#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/08/01 11:51:43 (UT+08:00) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# data file
file_data = 'hr.data'

# output file
file_output = 'hr.png'

# making empty lists for storing data
list_colour_BV = []
list_absmag_V  = []

# opening file for reading
with open (file_data, 'r') as fh_in:
    # reading file line-by-line
    for line in fh_in:
        # skipping line if the line starts with '#'
        if (line[0] == '#'):
            continue
        # splitting line
        (star, mag_str, colour_str, dist_str, absmag_str) = line.split ()
        # converting string into float
        mag_V     = float (mag_str)
        colour_BV = float (colour_str)
        dist_pc   = float (dist_str)
        absmag_V  = float (absmag_str)
        # appending data to lists
        list_colour_BV.append (colour_BV)
        list_absmag_V.append (absmag_V)

# creating Numpy arrays from lists
array_colour_BV = numpy.array (list_colour_BV)
array_absmag_V  = numpy.array (list_absmag_V)

# making a fig, canvas, and axes objects using object-oriented interface
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# making a plot using object-oriented interface
ax.plot (array_colour_BV, array_absmag_V, \
         linestyle='None', marker='o', markersize=3, color='r', \
         label='bright stars')
ax.invert_yaxis ()
ax.set_xlabel ('$B-V$ colour index')
ax.set_ylabel ('V-band absolute magnitude')
ax.legend ()
ax.grid ()

# making a PNG file
fig.savefig (file_output, dpi=150)
