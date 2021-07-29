from sympy import *
from sympy.abc import x as sympy_x, y as sympy_y

# Format entered function to string pyhton function
def format_fx(fx):
  #fx = re.sub("[a-z]", "x", fx)
  # Add constant e
  fx = fx.replace('e^(', 'exp(')
  # Replace ^ with **
  fx = fx.replace('^', '**')

  return fx

# Format py function to math string function
def format_fx_string(fx):
  #fx = re.sub("[a-z]", "x", fx)
  # Replace ^ with **
  fx = fx.replace('**', '^')
  # Add constant e
  fx = fx.replace('exp(', 'e^(')

  return fx

# Gest the derivative of a string function
def get_dx(fx, grade):
  return diff(fx, sympy_x, grade)

# Gest the integral of a string function
def get_integral_fx(fx):
  return integrate(fx, sympy_x)

# Solve a function equal to 0
def solve_function(fx):
  return solveset(fx, sympy_x)

# If number is complex, convert from sympy complex to python complext
def is_complex(num):
  if num.has(I):
    num = complex(num)
    return str(num)
  else:
    return float(num)

# Evaluate a string function in a given point
def evaluate_fx(fx, x):
  value = N( eval(fx) )
  value = is_complex(value)
  return value

# Gets absolute error
def absolute_error(xi, xf):
  return abs(xf - xi)