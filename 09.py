# -*- coding: utf-8 -*-
"""09

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VKGv-TovuTTMFdIsQpypb5Jk0ewS5zhw
"""

import numpy as np
import matplotlib.pyplot as plt
import time

N=10000
R=3
r=np.linspace(0, R, N)


def f1(r): #Density function for the Part 1
  return np.exp(-r**3)

def mass_tr_Sph(f, R,r,N): #mass function with the trapezoidal rule for spherical coordinate system
  dr=r[1]-r[0]
  I=(0.5*f(0)*r[0]**2+0.5*f(R)*r[-1]**2)*dr
  for k in range(1, N-1):
      I+=f(r[k])*dr*r[k]**2
  mass=4*np.pi*I
  return mass

def mass_mc_Sph(f, R,r,N): #mass function with the Monte-Carlo method for spherical coordinate system
  x=np.random.uniform(0, R, N)
  y=f(x)*x**2
  mass=4*np.pi*R*np.mean(y)
  return mass

def f2(x,y,z):
  return np.exp(-(x**2+y**2+z**2)**1.5)

def mass_tr_Rec(f,x,y,z):
    nx,ny,nz=len(x),len(y),len(z)
    hx,hy,hz=x[1]-x[0], y[1]-y[0], z[1]-z[0]
    I=0
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            for k in range(1, nz-1):
                I+=f(x[i], y[j], z[k])
    I+=0.5*(np.sum(f(x[0], y[1:-1], z[1:-1]))+np.sum(f(x[-1], y[1:-1], z[1:-1])))
    I+=0.5*(np.sum(f(x[1:-1], y[0], z[1:-1]))+np.sum(f(x[1:-1], y[-1], z[1:-1])))
    I+=0.5*(np.sum(f(x[1:-1], y[1:-1], z[0]))+np.sum(f(x[1:-1], y[1:-1], z[-1])))
    #value of the integrand at the eight corners:
    I+=0.125*(f(x[0], y[0], z[0])+f(x[-1], y[0], z[0])+f(x[0], y[-1], z[0])+f(x[-1], y[-1], z[0])+f(x[0], y[0], z[-1])+f(x[-1], y[0], z[-1])+f(x[0], y[-1], z[-1])+f(x[-1], y[-1], z[-1]))
    I*=hx*hy*hz
    return I

def mass_mc_Rec(f, a, b, N):
    V=(b-a)**3  #volume of a cube of side length 2R centered at the origin
    x=np.random.uniform(a, b, size=N)
    y=np.random.uniform(a, b, size=N)
    z=np.random.uniform(a, b, size=N)
    f_mean=np.mean(f(x, y, z))
    I=V*f_mean
    return I

"""###**Calculations**
###**Part I**
"""

mass_tr_Sph(f1,R,r,N)

mass_mc_Sph(f1,R,r,N)

epsilon=1e-3
start_time=time.time()
#Trapezoidal rule
N_trap=1
I_tr=mass_tr_Sph(f1,R,r,N_trap)
while abs(I_tr-4.18879020477)>epsilon:
    N_trap *= 2
    I_tr=mass_tr_Sph(f1,R,r,N_trap)
time_tr=time.time()-start_time

N_mc=1
I_mc=mass_mc_Sph(f1,R,r, N_mc)
while abs(I_mc-4.18879020477)>epsilon:
    N_mc*=2
    I_mc=mass_mc_Sph(f1,R,r, N_mc)
time_mc=time.time()-start_time

cost_tr=time_tr/N_trap
cost_mc=time_mc/N_mc

"""###**Part II**"""

x=np.linspace(-R, R, 101)
y=np.linspace(-R, R, 101)
z=np.linspace(-R, R, 101)
mass_tr_Rec(f2,x, y, z)

mass_mc_Rec(f2, -R, R, N)

start_time=time.time()
# Trapezoidal rule
N_tr2=2
x=np.linspace(-R, R, N_tr2)
y=np.linspace(-R, R, N_tr2)
z=np.linspace(-R, R, N_tr2)
I_tr2=mass_tr_Rec(f2,x, y, z)
while abs(I_tr2-4.18879020477)>epsilon:
    N_tr2*=2
    x=np.linspace(-R, R, N_tr2)
    y=np.linspace(-R, R, N_tr2)
    z=np.linspace(-R, R, N_tr2)
    I_tr2=mass_tr_Rec(f2,x, y, z)
time_tr2=time.time()-start_time
N_mc2=1
I_mc2=mass_mc_Rec(f2,-R,R,N_mc2)
while abs(I_mc2-4.18879020477)>epsilon:
    N_mc2*=2
    I_mc2=mass_mc_Rec(f2,-R,R,N_mc2)
time_mc2=time.time()-start_time

cost_tr2=time_tr2/N_tr2
cost_mc2=time_mc2/N_mc2

from tabulate import tabulate
table1 = [['Coord. System', 'Method', 'Num. of It.', 'Time', 'Cost'],
         ["Spherical", "Trapezoidal", N_trap, time_tr, cost_tr ],
         ["Spherical", "Monte Carlo", N_mc, time_mc, cost_mc],
         ["Rectangular", "Trapezoidal", N_tr2, time_tr2, cost_tr2],
         ["Rectangular", "Monte Carlo", N_mc2, time_mc2, cost_mc2]]

"""###**Results**
As it can be seen the trapezoidal rule was computationally more efficient for the first part than the Monte Carlo method, requiring significantly less time to achieve the same level of precision. While for the second part where 3 positional variables were given, MC method works much more efficiently. However, time taken for computation in both methods is significantly smaller for the Trapezoidal rule.
"""

print(tabulate(table1, headers='firstrow'))

"""###**Conclusion**
In conclusion, we have shown that numerical integration methods such as the trapezoidal rule and the Monte Carlo method can be used to compute the mass of a star, given its density function. It was  demonstrated that the Trapezoidal rule is more computationally efficient than the Monte Carlo method for the spherical coordinates. On the other hand, it was also figured out that the Monte Carlo method is more efficient for the rectangular method.
"""
