# Erick Lagunas-Rodriguez and Alita Rodriguez
# CST-305
# September 9, 2020
# Project 1
# To make this code, the ODE dp/dt = y/p was first made and
# from there it was solved using Odeint and Numpy. From
# there the data is graphed using pyplot
# Packages Used: matplotlib(pyplot), numpy, scipy(odient)

# Importing modules to graph and find the solution for the ODE
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dp/dt
def model(y,t,p):

    # ODE where dp/dt is the rate packets per second,
    # y is the throughput in bytes per second
    # and p is the packet size bytes per packet

    dpdt = y / p
    return dpdt

# initial throughput y
y0 = 125000000

# sets t to a linear array of numbers from 0 to 500
t = np.linspace(0,500)

# solve ODE with different packet sizes (p) using odeint
p = 84
y1 = odeint(model, y0, t, args=(p,))

p = 88
y2 = odeint(model, y0, t, args=(p,))

p = 92
y3 = odeint(model, y0, t, args=(p,))

# plot all three solutions in the same graph with a legend labeling each
plt.plot(t,y1,'r-',linewidth=2,label='p = 84')
plt.plot(t,y2,'b--',linewidth=2,label='p = 88 ')
plt.plot(t,y3,'g:',linewidth=2,label='p = 92')
plt.xlabel('time (s)')
plt.ylabel('packets')
plt.legend()
plt.show()