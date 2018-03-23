"""Created on Thu Mar 22 14:01:58 2018"""

"""@author: WeiJin, PoHan"""
"""This CES utility function was built according to Tresch, R. W. (2008). Public sector economics. Palgrave Macmillan."""

import math
import numpy as np

"""Define a simplified version of CES Utility Function"""
def CESuf(c,f):
  """Obtain all the attributes needed to compute utility"""
  """Obtain the consumption and factor bundle of an individual consumer"""
  c = np.array(c)
  f = np.array(f)
  """Obtain the other parameters"""
  y = np.array(0.8)
  b = np.array(0.5)
  s = np.array(0.7)
  a=[]
  t=[]
  for i in range(len(c)):
    a.append(0.2)
  for i in range(len(f)):
    t.append(0.5)
  a = np.array(a)
  t = np.array(t)
  
  """Define utility function, combining the consumption part and the factor part"""
  utility_subc = (np.dot((c ** y) , a)) ** ((1 - s) / y)
  utility_subf = np.dot((np.power(f , (t + 1))) , (b / (t + 1)))
  utility = utility_subc - utility_subf
  return utility

"""Input the attributes of the CES utility function"""
c = input("Please enter the consumption bundle(the quantities of your list of goods):")
f = input("Please enter the factors supplied(the quantities of your list of factors):")
print CESuf(c,f)