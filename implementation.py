import numpy as np
from numerical_approximators import ODE, integral

## ODE implementation
def f(x0,y0): return y0*np.cos(x0)

x_list = [i for i in range(10)] # list of the input x

#lists for accepting the output with a known first value 
y_e = np.zeros(len(x_list))
y_e[0]=1
y_h = np.zeros(len(x_list))
y_h[0]=1
y_mod = np.zeros(len(x_list))
y_mod[0]=1

ode = ODE(f)

y_e = ode.euler(x_list,y_e)
print(f"Euler: \n {y_e}")
y_h = ode.huen(x_list,y_h)
print(f"Huen: \n {y_h}")
y_mod = ode.modified_euler(x_list, y_mod)
print(f"Modified Euler: \n {y_mod}")

## Integral implementation

def F(x): return np.sin(x)

integrate = integral(F)
START = 0
END = 2

y_trap = integrate.trapezoid(START,END)
print(f"Trapezoid: \n {y_trap}")
y_comp_trap= integrate.composite_trapezoid(START,END,4)
print(f"Composite Trapezoid: \n {y_comp_trap}")
y_simp = integrate.simpsons(START,END)
print(f"Simpsons: \n {y_simp}")
y_comp_simp = integrate.composite_simpsons(START,END,8)
print(f"Composite Simpsons: \n {y_comp_simp}")

CACHE = {}
y_romberg = integrate.romberg(0,np.pi/2,2,1,CACHE)
print(f"Romberg traces: \n {CACHE}")
