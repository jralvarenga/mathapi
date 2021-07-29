import json

from sympy import *
from math import gcd
from django.http import HttpResponse

def define_phi(n):
  amount = 0        
  for k in range(1, n + 1):
    if gcd(n, k) == 1:
      amount += 1
  return amount

def phi_function(req):
  body = json.loads( req.body.decode('utf-8') )
  n = body['n']

  phi = define_phi(n)

  data = {
    'phi': float(phi)
  }

  res = json.dumps(data)
  return HttpResponse(res, content_type="application/json")
