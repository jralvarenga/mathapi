import json

from mathapi.lib.math_ops import absolute_error, evaluate_fx, format_fx, get_dx
from django.http import HttpResponse

def trapz_simple(fx, a, b):
  fa = evaluate_fx(fx, a)
  fb = evaluate_fx(fx, b)
  dx = get_dx(fx, 2)
  dab = evaluate_fx(str(dx), a)
  value = (b - a)*(fa + fb)/2

  error = (-1/12)*(dab)*((b - a)**3)
  return {
    'integral': value,
    'error': round(abs(error), 3)
  }

def trapz_composite(fx, a, b, iterations):
  fa = evaluate_fx(fx, a)
  fb = evaluate_fx(fx, b)
  dx = get_dx(fx, 2)
  dab = evaluate_fx(str(dx), 0)

  h = (b - a)/iterations
  fafb = (fa + fb)/2
  sumatory = 0

  for i in range(0, iterations):
    eval_value = a + i*h
    f_eval = evaluate_fx(fx, eval_value)
    sumatory = f_eval + sumatory

  value = h*( (fafb) + sumatory )
  error = -( ((b - a)**3)/(12*(iterations**2)) * (dab) )
  
  return {
    'integral': value,
    'error': round(abs(error), 3)
  }

def trapz_pairs(x, y):
  n = len(x)
  value = 0

  for i in range(1, n):
    a = x[i - 1]
    b = x[i]
    h = b - a

    value = (h/2)*(y[i - 1] + y[i]) + value

  return {
    'integral': value,
    'error': 0.0
  }

def trapz_method(req):
  # Get params
  params = req.GET
  type = params.get('type')
  iterations = int(params.get('iterations')) if params.get('iterations') != None else 100

  # Get body
  body = json.loads( req.body.decode('utf-8') )

  if type == 'simple':
    fx = body['fx']
    fx = format_fx(fx)
    a = body['a']
    b = body['b']
    data = trapz_simple(fx, a, b)
  elif type == 'composite':
    fx = body['fx']
    fx = format_fx(fx)
    a = body['a']
    b = body['b']
    data = trapz_composite(fx, a, b, iterations)
  elif type == 'ordered_pairs':
    x = body['x']
    y = body['y']
    data = trapz_pairs(x, y)
  else:
    fx = body['fx']
    fx = format_fx(fx)
    a = body['a']
    b = body['b']
    data = trapz_composite(fx, a, b, iterations)

  res = json.dumps(data)
  return HttpResponse(res, content_type="application/json")