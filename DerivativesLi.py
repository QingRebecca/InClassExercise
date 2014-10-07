#In class exercise: Derivative
#Author: Rebecca Li
import numpy as np
import pylab as pl

def f(x):
    return x**3-np.sin(x)

def df(x):
    return 3*x**2-np.cos(x)

###################### Exercise 1
print '############# Exercise 1'

h =0.001
x =2.0

dfor = (f(x+h)-f(x))/h
print 'The derivative abtained by forward difference is %.5f'%dfor

dcenter = (f(x+h/2.0)-f(x-h/2))/h
print 'The derivative abtained by center difference is %.5f'%dcenter

efor = (dfor-df(x))/df(x)*100
print 'The error of the forward difference is %.6f%%' %efor

ecen = (dcenter-df(x))/df(x)*100
print 'The error of the forward difference is %.6f%%' %ecen

##################### Exercise 2
def x(t):
    return 3*t**2-2*t+1

m = 0.8
t =1.5
F = m*(x(t+h/2.0)-x(t-h/2.0))/h
print '############### Exercise 2'
print "The force exerted on the book is %.2f N" %F

#################### Exercise 3
print '###############Exercise 3'
def dxdt(x,t):
    return x**3+x*np.sin(t)+1
x =0
xpoints =[]
dt = 0.001
tpoints = np.arange(0,1,dt)
for t in tpoints:
    xpoints.append(x)
    x += dt*dxdt(x,t)
    
pl.plot(tpoints,xpoints)
pl.show()
