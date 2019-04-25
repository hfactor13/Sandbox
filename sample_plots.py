import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
import sympy as sp
from sympy import Eq, sympify
plt.close('all')

# Sample Plot 1 (Decaying Sinusoidal Plot)
t = np.linspace(0, 2*np.pi, 100)
x = np.exp(-t)*np.sin(t)

fig1 = plt.figure()
ax1 = fig1.gca()
ax1.plot(t, x, 'r-')
ax1.set(xlabel = 'time', ylabel = 'Response', title = 'Decaying Sinusoidal Plot', \
        xlim = (0, 2*np.pi))

# Sample Plot 2 (Bode Plot)
fig2 = plt.figure()
ax2 = fig2.gca()
H = ctrl.tf([1, 1], [1, -2, 1])

## Transfer function for the bode plot
s = sp.symbols('s')
Hsym = (s + 1)/(s**2 - 2*s + 1)
sp.init_printing(prettyprint = True)
sp.pprint(Eq(sympify('H(s)'), Hsym))

## Bode Plot of H(s)
ctrl.bode(H, dB = True)

## Step Response Plot of H(s)
fig3 = plt.figure()
ax3 = fig3.gca()
T, yout = ctrl.step_response(H)
plt.plot(T, yout)