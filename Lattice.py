'''Lattice Model
  Author: Rebecca Li
  Date: September 17,2014
  This program is designed to simulate the sodium chlorine lattice and iron lattice.'''
  

from visual import *
import numpy as np

R=0.3   #Set all the radius of atoms as R = 0.3
positions_sodium = [] # Create an empty list for the positions of sodium atoms
positions_chlorine = [] # Create an empty list fot the positions of chlorine atoms

display(title='Sodium Chlorine Lattice and Iron Lattice')  # Make a title for the graph

'''In the following loop, we iterate every position in a range of space ,
   and destribute those whose sum of x,y,z is even to sodium atoms while those whose
   sum of x, y, z is odd to chlorine atoms.'''
for i in range(-10,-0):   
    for j in range(-10,-0):
        for k in range(10):
            if (i+j+k)%2 ==0:
                positions_sodium.append([i,j,k])
            else:
                positions_chlorine.append([i,j,k])

# In the loops below, we generate a white sphere atom at every position in the list of sodium positions 
# and a blue sphere at every position in the list of chlorine positions
for i in range(len(positions_sodium)):
    sphere(radius = R, pos = positions_sodium[i],color=color.white)

for i in range(len(positions_chlorine)):
    sphere(radius = R, pos = positions_chlorine[i],color = color.blue)


positions_iron=[]

for i in range(10):
    for j in range(10):
        for k in range(10):
            if (i+j+k)%2 != 0:
                positions_iron.append([i,j,k])

for i in range(len(positions_iron)):
    sphere(radius = R, pos = positions_iron[i],color = [0,1,1])
