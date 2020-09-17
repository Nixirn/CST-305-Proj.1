
#import the required modules
import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import odeint

def model(x, t, k):
#    k = 84 #define a constant, can be commented out for args
    dydt = 1/k #the differential equation
    return dydt

#initial condition
y0 = 0

#time points
t= np.linspace(0,20)

#solve ODEs
k=84
y1 = odeint(model, y0, t, args=(k,)) #function that solves the function described above
k = 88
y2 = odeint(model, y0, t, args=(k,))
k=92
y3 = odeint(model,y0,t, args=(k,))

#get or set the limits of the independent variable, speed
#plt.xlim(1250000,125000000)
#plt.ylim(14000,1400000)
#plot results
plt.plot(t,y1, 'r-',linewidth=2,label='k=84 bytes per packet')
plt.plot(t,y2,'b-',linewidth=2,label='k=88 bytes per packet')
plt.plot(t,y3,'g:',linewidth=2,label='k=92 bytes per packet')
plt.xlabel('speed (bytes/second)')
plt.ylabel('y(t) packets per second')
plt.legend()
plt.show()

