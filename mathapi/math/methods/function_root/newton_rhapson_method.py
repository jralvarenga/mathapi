import json

from mathapi.lib.math_ops import absolute_error, evaluate_fx, format_fx, get_dx
from django.http import HttpResponse

def apply_method(fx, dx, xi, tolerancy):
  k = 0
  error = 1

  while error > tolerancy:
    dxi = evaluate_fx(dx, xi)
    fxi = evaluate_fx(fx, xi)
    if dxi != 0:
      xf = xi - ( fxi/dxi )
      error = absolute_error(xi, xf)

      xi = xf
    else:
      return { 'error': 'error' }

    k = k + 1

  return {
    'root': xf,
    'iterations': k
  }

def apply_method_with_iteration(fx, dx, xi, tolerancy):
  k = 0
  error = 1
  values = []

  while error > tolerancy:
    dxi = evaluate_fx(dx, xi)
    fxi = evaluate_fx(fx, xi)
    if dxi != 0:
      xf = xi - ( fxi/dxi )
      values.append({
        'value': xf,
        'iteration': k
      })
      error = absolute_error(xi, xf)

      xi = xf
    else:
      return { 'error': 'error' }

    k = k + 1
  
  return values


def newton_rhapson_method(req):
  # Get params
  params = req.GET
  format = params.get('format')
  tolerancy = params.get('tolerancy')

  # Get body
  body = json.loads( req.body.decode('utf-8') )
  fx = body['fx']

  fx = format_fx(fx)
  dx = get_dx(fx, 1)
  dx = str(dx)
  xi = body['xi']

  if tolerancy != None:
    tolerancy = float(tolerancy) / 100
  else:
    tolerancy = 0

  if format == 'every_iteration':
    data = apply_method_with_iteration(fx, dx, xi, tolerancy)
  else:
    data = apply_method(fx, dx, xi, tolerancy)

  res = json.dumps(data)
  return HttpResponse(res, content_type="application/json")