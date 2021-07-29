import json

from mathapi.lib.math_ops import format_fx, format_fx_string
from sympy import *
from sympy.abc import x as sympy_x
from django.http import HttpResponse

def integral_evaluate(req):
  # Get params
  params = req.GET
  order = params.get('order')
  order = int(order) if order else 1

  # Get body
  body = json.loads( req.body.decode('utf-8') )
  fx = body['fx']
  a = body['a']
  b = body['b']
  fx = format_fx(fx)

  if a == 'inf':
    a = oo
  if b == 'inf':
    b = oo

  integral = integrate(fx, (sympy_x, a, b))
  integral = format_fx_string(str(integral))

  data = {
    'integral': str(integral),
  }

  res = json.dumps(data)
  return HttpResponse(res, content_type="application/json")