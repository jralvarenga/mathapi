import json

from mathapi.lib.math_ops import absolute_error, evaluate_fx, format_fx, get_dx
from django.http import HttpResponse

def apply_method(fx, d1x, d2x, xi, tolerancy):
  k = 0
  error = 1

  while error > tolerancy:
    fxi = evaluate_fx(fx, xi)
    d1xi = evaluate_fx(str(d1x), xi)
    d2xi = evaluate_fx(str(d2x), xi)

    xn = xi - (2*fxi*d1xi)/(2*(d1xi**(2)) - fxi*d2xi)
    error = absolute_error(xi, xn)

    xi = xn
    k = k + 1

  return {
    'root': xn,
    'iterations': k
  }

def apply_method_with_iteration(fx, d1x, d2x, xi, tolerancy):
  k = 0
  error = 1
  values = []

  while error > tolerancy:
    fxi = evaluate_fx(fx, xi)
    d1xi = evaluate_fx(str(d1x), xi)
    d2xi = evaluate_fx(str(d2x), xi)

    xn = xi - (2*fxi*d1xi)/(2*(d1xi**(2)) - fxi*d2xi)
    values.append({
      'value': xn,
      'iteration': k
    })
    error = absolute_error(xi, xn)

    xi = xn
    k = k + 1
  
  return values

def halley_method(req):
  # Get params
  params = req.GET
  format = params.get('format')
  tolerancy = params.get('tolerancy')

  # Get body
  body = json.loads( req.body.decode('utf-8') )
  fx = body['fx']
  
  fx = format_fx(fx)
  xi = body['xi']
  d1x = get_dx(fx, 1)
  d2x = get_dx(fx, 2)

  if tolerancy != None:
    tolerancy = float(tolerancy) / 100
  else:
    tolerancy = 0

  if format == 'every_iteration':
    data = apply_method_with_iteration(fx, d1x, d2x, xi, tolerancy)
  else:
    data = apply_method(fx, d1x, d2x, xi, tolerancy)

  res = json.dumps(data)
  return HttpResponse(res, content_type="application/json")