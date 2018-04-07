#! /usr/bin/env python
import numpy as np
import json
import sys
from scipy import interpolate

write_txt = False
subsampling_rate = 0.05
jitter_scale = 0.5

def spherical_to_cartesian(x, y):
    # Weird convention. Computer scientists?
    phi = x/180.0*np.pi;
    if phi < 0: phi = phi + 2*np.pi;
    phi = phi + 90.0/180.0*np.pi;
    theta = -1*(y / 180.0*np.pi) + np.pi*0.5;           
    zsph = np.sin(theta)*np.cos(phi);
    xsph = np.sin(theta)*np.sin(phi);
    ysph = np.cos(theta);
    return np.array([zsph, xsph, ysph])

# Read raw
ifs = open(sys.argv[1])
coords = []
for ln in ifs.readlines():
    coords = coords + ln[:-1].split()
# Load coordinates
xs = []
ys = []
ts = []
locations = []
for c in coords:
    x, y, z = tuple(map(float, c.split(',')))
    xs.append(x)
    ys.append(y)
xs = np.array(xs)
ys = np.array(ys)
# Time parameter
ts = np.arange(0, xs.shape[0])

# Interpolate (need to convert phi first to deal with -180 +180 discontinuity)
x1s = np.cos(xs/180.*np.pi)
x2s = np.sin(xs/180.*np.pi)
if write_txt:
    np.savetxt('coords.txt', 
        np.array([xs,ys,x1s,x2s,np.arctan2(x2s,x1s)*180/np.pi]).T)
fx1 = interpolate.interp1d(ts, x1s, kind='quadratic')
fx2 = interpolate.interp1d(ts, x2s, kind='quadratic')
fy  = interpolate.interp1d(ts, ys,  kind='quadratic')
# Fine-grained time axis
tts = np.arange(0, x1s.shape[0]-1, subsampling_rate)
x1s = fx1(tts)
x2s = fx2(tts)
xs = np.arctan2(x2s,x1s)*180/np.pi
ys = fy(tts)
if write_txt:
    np.savetxt('coords_interp1d.txt', np.array([xs,ys]).T)
# Add jitter
jitter_x = jitter_scale*(np.random.uniform(size=xs.shape[0])-0.5)
jitter_y = jitter_scale*(np.random.uniform(size=ys.shape[0])-0.5)
xs = xs+jitter_x
ys = ys+jitter_y

# Total time taken in [s] at velocity v
v = 1.0 # *6370 km/s
T = 0.0
for i in range(xs.shape[0]-1):
    r1 = spherical_to_cartesian(xs[i], ys[i])
    r2 = spherical_to_cartesian(xs[i+1], ys[i+1])
    dr = np.dot(r2-r1, r2-r1)**0.5
    dt = dr/v
    T += dt

# Output
locations = []
t = 0.0
for i in range(xs.shape[0]-1):
    r1 = spherical_to_cartesian(xs[i], ys[i])
    r2 = spherical_to_cartesian(xs[i+1], ys[i+1])
    dr = np.dot(r2-r1, r2-r1)**0.5
    dt = dr/v
    locations.append({
        "x": int(xs[i]*1e7),
        "y": int(ys[i]*1e7),
        "t": (t/T)*24, #float(i)/xs.shape[0]*24
    })
    t += dt
json.dump({ "locations": locations }, open(sys.argv[1][:-4]+'.json', 'w'), indent=1)












    
