import json

from sympy import *
from django.http import HttpResponse

def beta_function(req):
  body = json.loads( req.body.decode('utf-8') )
  x = body['x']
  y = body['y']
  x = eval(str(x))
  y = eval(str(y))
  
  gamma_x = gamma(x)
  gamma_y = gamma(y)

  beta = (gamma_x * gamma_y) / (gamma(x + y))

  data = {
    'beta': float(beta)
  }

  res = json.dumps(data)
  return HttpResponse(res, content_type="application/json")
