import json

from mathapi.lib.math_ops import absolute_error, evaluate_fx, format_fx
from django.http import HttpResponse

def apply_method(f, a, b, tolerancy):
  k = 0
  error = 1

  while error >= tolerancy:
    x = (a + b) / 2
    fx = evaluate_fx(f, x)
    fa = evaluate_fx(f, a)
    error = absolute_error(a, x)

    if fx * fa < 0:
      b = x
    elif fx * fa > 0:
      a = x
    elif fx == 0:
      break
    
    k = k + 1

  return {
    'root': x,
    'iterations': k
  }

def apply_method_with_iteration(f, a, b, tolerancy):
  k = 0
  values = []
  error = 1

  while error >= tolerancy:
    x = (a + b) / 2
    error = absolute_error(a, x)
    values.append({
      'iteration': k,
      'value': x
    })
    fx = evaluate_fx(f, x)
    fa = evaluate_fx(f, a)

    if fx * fa < 0:
      b = x
    elif fx * fa > 0:
      a = x
    elif fx == 0:
      break

    k = k + 1
  
  return values

def bisection_method(req):
  # Get params
  params = req.GET
  format = params.get('format')
  tolerancy = params.get('tolerancy')

  # Get body
  body = json.loads( req.body.decode('utf-8') )
  fx = body['fx']
  
  fx = format_fx(fx)
  a = body['a']
  b = body['b']

  if tolerancy != None:
    tolerancy = float(tolerancy) / 100
  else:
    tolerancy = 0

  fa = evaluate_fx(fx, a)
  fb = evaluate_fx(fx, b)

  if (fa * fb) < 0:

    if format == 'every_iteration':
      data = apply_method_with_iteration(fx, a, b, tolerancy)
    else:
      data = apply_method(fx, a, b, tolerancy)

    res = json.dumps(data)
    return HttpResponse(res, content_type="application/json")
  else: 
    return HttpResponse('error')