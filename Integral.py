#Author: Rebecca Li
'''In class exericse: Given the velocity from t = 0 to t=100,
use trapezoidal rule to calaulate the approximate
integral(distance) over time and make a position vs. time graph
'''

import numpy as np
import pylab as pl

data = np.loadtxt('velocity.txt')
t = data[:,0]
v = data[:,1]
pl.plot(t,v)



N = len(t)
a = t[0]
b = t[100]
S = (v[0]+v[100])/2
step = (t[100]-t[0])/(N-1)

X = []
for i in range(0,N):
    new_t = a+i*step
    X.append(S*step)
    S += v[new_t]
    
    
print 'The integral is %5.2f' %S*step
pl.plot(t,X)
pl.legend(['velocity','position'])
pl.xlabel('time')
pl.ylabel('position & velocity')
pl.show()

