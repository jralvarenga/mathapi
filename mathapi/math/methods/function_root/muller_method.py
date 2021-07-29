import json
import math

from mathapi.lib.math_ops import absolute_error, evaluate_fx, format_fx
from django.http import HttpResponse

def apply_method(fx, x0, x1, x2, tolerancy):
  k = 0
  error = 1

  while error >= tolerancy:
    fx0 = evaluate_fx(fx, x0)
    fx1 = evaluate_fx(fx, x1)
    fx2 = evaluate_fx(fx, x2)
    h1 = x1 - x0
    h2 = x2 - x1

    delta1 = (fx1 - fx0)/h1
    delta2 = (fx2 - fx1)/h2

    a = (delta2 - delta1)/(h2 + h1)
    b = a*h2 + delta2
    c = fx2

    xn = x2 + (-2*c)/(b + math.sqrt( b**(2) - 4*a*c ))
    error = absolute_error(x2, xn)

    x0, x1, x2 = x1, x2, xn
    k = k + 1

  return {
    'root': xn,
    'iterations': k
  }

def apply_method_with_iteration(fx, x0, x1, x2, tolerancy):
  k = 0
  error = 1
  values = []

  while error >= tolerancy:
    fx0 = evaluate_fx(fx, x0)
    fx1 = evaluate_fx(fx, x1)
    fx2 = evaluate_fx(fx, x2)
    h1 = x1 - x0
    h2 = x2 - x1

    delta1 = (fx1 - fx0)/h1
    delta2 = (fx2 - fx1)/h2

    a = (delta2 - delta1)/(h2 + h1)
    b = a*h2 + delta2
    c = fx2

    xn = x2 + (-2*c)/(b + math.sqrt( b**(2) - 4*a*c ))
    values.append({
      'value': xn,
      'iteration': k
    })
    error = absolute_error(x2, xn)

    x0, x1, x2 = x1, x2, xn
    k = k + 1
  
  return values

def muller_method(req):
  # Get params
  params = req.GET
  format = params.get('format')
  tolerancy = params.get('tolerancy')

  # Get body
  body = json.loads( req.body.decode('utf-8') )
  fx = body['fx']
  
  fx = format_fx(fx)
  x0 = body['x0']
  x1 = body['x1']
  x2 = body['x2']

  if tolerancy != None:
    tolerancy = float(tolerancy) / 100
  else:
    tolerancy = 0.001

  if format == 'every_iteration':
    data = apply_method_with_iteration(fx, x0, x1, x2, tolerancy)
  else:
    data = apply_method(fx, x0, x1, x2, tolerancy)

  res = json.dumps(data)
  return HttpResponse(res, content_type="application/json")