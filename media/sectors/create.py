#! /usr/bin/env python
import os

# Input resolution of main.jpg
X = 21600
Y = 10800

# Split onto chunks of size:
dx = 5400
dy = 5400

nx = X/dx
ny = Y/dy

for i in range(nx):
    for j in range(ny):
        print i, j
        x0 = i*dx
        y0 = j*dx
        os.system('convert main.jpg -crop %dx%d+%d+%d -scale 4096 sec_4096_%d_%d.jpg' % (dx, dy, x0, y0, i, j))

