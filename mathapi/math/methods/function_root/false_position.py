import json

from mathapi.lib.math_ops import absolute_error, evaluate_fx, format_fx
from django.http import HttpResponse

def apply_method(fx, xi, xf, tolerancy):
  k = 0
  error = 1

  while error >= tolerancy:
    fxi = evaluate_fx(fx, xi)
    fxf = evaluate_fx(fx, xf)

    xr = xi - (fxi*( (xf - xi)/(fxf - fxi) ))
    error = absolute_error(xf, xr)

    xi, xf = xf, xr
    k = k + 1

  return {
    'root': xr,
    'iterations': k
  }


def apply_method_with_iteration(fx, xi, xf, tolerancy):
  k = 0
  error = 1
  values = []

  while error >= tolerancy:
    fxi = evaluate_fx(fx, xi)
    fxf = evaluate_fx(fx, xf)

    xr = xi - (fxi*( (xf - xi)/(fxf - fxi) ))
    values.append({
      'value': xr,
      'iteration': k
    })
    error = absolute_error(xf, xr)

    xi, xf = xf, xr
    k = k + 1
  
  return values


def false_position_method(req):
  # Get params
  params = req.GET
  format = params.get('format')
  tolerancy = params.get('tolerancy')

  if tolerancy != None:
    tolerancy = float(tolerancy) / 100
  else:
    tolerancy = 0.001

  # Get body
  body = json.loads( req.body.decode('utf-8') )
  fx = body['fx']
  
  fx = format_fx(fx)
  xi = body['xi']
  xf = body['xf']

  if format == 'every_iteration':
    data = apply_method_with_iteration(fx, xi, xf, tolerancy)
  else:
    data = apply_method(fx, xi, xf, tolerancy)

  res = json.dumps(data)
  return HttpResponse(res, content_type="application/json")