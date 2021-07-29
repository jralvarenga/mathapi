import json
from mathapi.lib.math_ops import evaluate_fx, format_fx, absolute_error
from django.http import HttpResponse

def apply_method(fx, x0, tolerancy):
  k = 0
  error = 1

  while error >= tolerancy:
    fx0 = evaluate_fx(fx, x0)
    fx0_fx0 = evaluate_fx(fx, x0 + fx0)

    if (fx0_fx0 - fx0) != 0:
      x = x0 -( (fx0**(2)) / (fx0_fx0 - fx0) )
      error = absolute_error(x0, x)
    else:
      break

    x0 = x
    k = k + 1

  x = x0
  return {
    'root': x,
    'iterations': k
  }


def apply_method_with_iteration(fx, x0, tolerancy):
  k = 0
  values = []
  error = 1

  while error >= tolerancy:
    fx0 = evaluate_fx(fx, x0)
    fx0_fx0 = evaluate_fx(fx, x0 + fx0)

    if (fx0_fx0 - fx0) != 0:
      x = x0 -( (fx0**(2)) / (fx0_fx0 - fx0) )
      values.append({
        'value': x,
        'iteration': k
      })
      error = absolute_error(x0, x)
    else:
      break

    x0 = x
    k = k + 1
  
  return values


def steffensen_method(req):
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