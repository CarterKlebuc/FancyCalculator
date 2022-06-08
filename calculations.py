from sympy import *
from numpy import linspace

def in_integral_calc(result):
  x = Symbol('x')
  Answer = integrate(parse_expr(result))
  Answer = str(Answer) + ' + c'
  return Answer

def def_integral_calc(result, upper_bound, lower_bound):
  x = Symbol('x')
  Answer = integrate(parse_expr(result), (x, lower_bound, upper_bound))
  Answer = str(Answer)
  return Answer

def derivative_calc(result):
  x = Symbol('x')
  Answer = diff(parse_expr(result))
  Answer = str(Answer)
  return Answer

