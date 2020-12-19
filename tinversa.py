# import inverse_laplace_transform 
from sympy.integrals.transforms import inverse_laplace_transform 
from sympy import exp, Symbol 
from sympy.abc import s, t 
  
a = Symbol('a', positive = True) 
# Using inverse_laplace_transform() method 
gfg = inverse_laplace_transform(exp(-a * s)/s, s, 5) 
  
print(gfg)
