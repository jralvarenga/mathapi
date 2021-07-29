import json

from mathapi.lib.math_ops import absolute_error, evaluate_fx, format_fx
from django.http import HttpResponse

def apply_method(fx, x0, tolerancy):
  k = 0
  error = 1

  while error > tolerancy:
    xr = evaluate_fx(fx, x0)
    error = absolute_error(x0, xr)
    
    x0 = xr
    k = k + 1
  
  return {
    'root': x0,
    'iterations': k
  }

def apply_method_with_iteration(fx, x0, tolerancy):
  k = 0
  error = 1
  values = []

  while error > tolerancy:
    xr = evaluate_fx(fx, x0)
    values.append({
      'value': x0,
      'iteration': k
    })
    error = absolute_error(x0, xr)
    
    x0 = xr

    k = k + 1
    
  return values

def fixed_point_method(req):
  # Get params
  params = req.GET
  format = params.get('format')
  tolerancy = params.get('tolerancy')

  # Get body
  body = json.loads( req.body.decode('utf-8') )
  fx = body['fx']

  fx = format_fx(fx)
  x0 = body['x0']

  if tolerancy != None:
    tolerancy = float(tolerancy) / 100
  else:
    tolerancy = 0

  if format == 'every_iteration':
    data = apply_method_with_iteration(fx, x0, tolerancy)
  else:
    data = apply_method(fx, x0, tolerancy)
  
  res = json.dumps(data)
  return HttpResponse(res, content_type="application/json")