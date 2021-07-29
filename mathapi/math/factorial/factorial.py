import json

from sympy import *
from django.http import HttpResponse

def factorial(req):
  body = json.loads( req.body.decode('utf-8') )
  n = body['n']
  n = eval(str(n))
  value = gamma(n + 1)

  data = {
    'factorial': float(value)
  }

  res = json.dumps(data)
  return HttpResponse(res, content_type="application/json")
