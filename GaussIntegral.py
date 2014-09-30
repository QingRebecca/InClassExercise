# Rebecca Li
# In class exercise

from gaussxw import gaussxwab

#define the function we are going to integrate
def f(x):
    return x**4-2*x+1

N = 13   # N-th order Gaussian intergration 
a = 0    # Starting point
b = 2    # Ending point
x,w = gaussxwab(N,a,b) # Use the function gaussxwab to get the integration
                        # point x and its weight mapped to the interval [a,b]


I = 0  # Set the initial integral as 0
for i in range(N):   # Integrate
    I += f(x[i])*w[i]

print 'The intergral is %5.17f' %I
