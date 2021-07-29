import json
from mathapi.lib.math_ops import absolute_error, evaluate_fx, format_fx
from django.http import HttpResponse


def apply_method(f, x0, x1, tolerancy):
  k = 0
  error = 1

  while error >= tolerancy:
    fx0 = evaluate_fx(f, x0)
    fx1 = evaluate_fx(f, x1)
    diff_f = fx1 - fx0
    if diff_f != 0:
      x2 = x1 - ( (fx1 * (x1 - x0)) / diff_f)
      error = absolute_error(x2, x1)
      x0, x1 = x1, x2
      k = k + 1
    else:
      break
  
  return {
    'root': x2,
    'iterations': k
  }


def apply_method_with_iteration(f, x0, x1, tolerancy):
  k = 0
  values = []
  error = 1

  while error >= tolerancy:
    fx0 = evaluate_fx(f, x0)
    fx1 = evaluate_fx(f, x1)
    diff_f = fx1 - fx0
    if diff_f != 0:
      x2 = x1 - ( (fx1 * (x1 - x0)) / diff_f)
      values.append({
        'value': x2,
        'iteration': k
      })
      error = absolute_error(x2, x1)
      
      x0, x1 = x1, x2
      k = k + 1
    else:
      break
  
  return values


def secant_method(req):
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
  
  if tolerancy != None:
    tolerancy = float(tolerancy) / 100
  else:
    tolerancy = 0
  
  fx0 = evaluate_fx(fx, x0)
  fx1 = evaluate_fx(fx, x1)

  if (fx0 - fx1) != 0:

    if format == 'every_iteration':
      data = apply_method_with_iteration(fx, x0, x1, tolerancy)
    else:
      data = apply_method(fx, x0, x1, tolerancy)
    
    res = json.dumps(data)
    return HttpResponse(res, content_type="application/json")
  else:
    return HttpResponse('error')