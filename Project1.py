import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dx/dt

def model(y,t,p):
    dpdt = y / p
    return dpdt

# initial condition
y0 = 125000000

# time points
t = np.linspace(0,500)

# solve ODE
p = 84
y1 = odeint(model,y0,t,args=(p,))
p = 88
y2 = odeint(model,y0,t,args=(p,))
p = 92
y3 = odeint(model,y0,t,args=(p,))

# plot results
plt.plot(t,y1,'r-',linewidth=2,label='p = 84')
plt.plot(t,y2,'b--',linewidth=2,label='p = 88 ')
plt.plot(t,y3,'g:',linewidth=2,label='p = 92')
plt.xlabel('time')
plt.ylabel('p(t)')
plt.legend()
plt.show()