import json

from mathapi.lib.math_ops import absolute_error, evaluate_fx, format_fx, get_dx
from django.http import HttpResponse

# Simpson's rule 1/3 simple
def simpson_13_simple(fx, a, b):
  m = (a + b)/2
  fa = evaluate_fx(fx, a)
  fb = evaluate_fx(fx, b)
  fm = evaluate_fx(fx, m)

  value = ((b - a)/6)*(fa + 4*fm + fb)

  h = (b - a)/2
  d4x = get_dx(fx, 4)
  d4e = evaluate_fx(str(d4x), ((b + a)/2))
  error = (-(h**(5))/90)*d4e

  return {
    'integral': value,
    'error': abs(round(error, 3))
  }

# Simpson's rule 1/3 composite
def simpson_13_composite(fx, a, b, n):
  fa = evaluate_fx(fx, a)
  fb = evaluate_fx(fx, b)
  h = (b - a) / n

  sum_1 = 0
  sum_2 = 0
  
  for i in range(1,n):
    c = a + i*h
    fc = evaluate_fx(fx, c)
    
    if i%2 == 0:
      # Sumatory 1
      sum_1 = fc + sum_1
    else:
      # Sumatory 1
      sum_2 = fc + sum_2
  
  value = (h/3)*(fa + 2*sum_1 + 4*sum_2 + fb)
  d4x = get_dx(fx, 4)
  d4e = evaluate_fx(str(d4x), ((b + a)/2))
  error = ((b - a)*(h**(4))/180)*d4e
  
  return {
    'integral': value,
    'error': abs(round(error, 3))
  }

# Simpson's rule 3/8 simple
def simpson_38_simple(fx, a, b):
  h = (b - a)/3
  fa = evaluate_fx(fx, a)
  fb = evaluate_fx(fx, b)

  f_1 = evaluate_fx(fx, (2*a + b)/3)
  f_2 = evaluate_fx(fx, (2*b + a)/3)

  value = (3*h/8)*(fa + 3*f_1 + 3*f_2 + fb)
  d4x = get_dx(fx, 4)
  d4e = evaluate_fx(str(d4x), ((b + a)/2))
  error = -(3/80)*(h**(5))*d4e

  return {
    'integral': value,
    'error': abs(round(error, 3))
  }

# Simpson's rule 3/8 composite
def simpson_38_composite(fx, a, b, n):
  fa = evaluate_fx(fx, a)
  fb = evaluate_fx(fx, b)
  h = (b - a) / n
  sum_1 = 0
  sum_2 = 0
  
  for i in range(1,n):
    c = a + i*h
    fc = evaluate_fx(fx, c)
    
    if i%2 == 0:
      # Sumatory 1
      sum_1 = fc + sum_1
    else:
      # Sumatory 1
      sum_2 = fc + sum_2
  
  value = (3*h/8)*(fa + 2*sum_1 + 3*sum_2 + fb)
  d4x = get_dx(fx, 4)
  d4e = evaluate_fx(str(d4x), ((b + a)/2))
  error = (n/80)*(h**(5))*d4e

  return {
    'integral': value,
    'error': abs(round(error, 3))
  }

# Simpson 1/3 rule with pairs
def simpson_pairs_13(x, y):
  n = len(x)
  value = 0
  sum_1 = y[0] + y[-1]
  sum_2 = 0
  sum_3 = 0
  h = 0
  count = 0

  for i in range(1, n, 2):
    limit = x[i] - x[i - 1]
    h = h + limit
    count = count + 1

  for i in range(1, n-1):
    if (i % 2) == 0:
      # Sumatory 3
      sum_3 = sum_3 + (y[i])
    else:
      # Sumatory 2
      sum_2 = sum_2 + (y[i])

  h = h/count
  value = (h/3)*(sum_1 + 4*sum_2 + 2*sum_3)

  return {
    'integral': value,
    'error': abs(0)
  }

# Simpson 3/8 rule with pairs
def simpson_pairs_38(x, y):
  n = len(x)
  value = 0
  sum_1 = y[0] + y[-1]
  sum_2 = 0
  sum_3 = 0
  h = 0
  count = 0

  for i in range(1, n, 2):
    limit = x[i] - x[i - 1]
    h = h + limit
    count = count + 1

  for i in range(3, n - 1, 3):
    sum_2 = sum_2 + y[i]

  for i in range(0, n-1):
    if (i % 3) != 0:
      # Sumatory 3
      sum_3 = sum_3 + (y[i])

  h = h/count
  value = (3*h/8)*(sum_1 + 2*sum_2 + 3*sum_3)

  return {
    'integral': value,
    'error': abs(0)
  }


def simpson_method(req):
  # Get params
  params = req.GET
  type = params.get('type')
  iterations = int(params.get('iterations')) if params.get('iterations') != None else 100

  # Get body
  body = json.loads( req.body.decode('utf-8') )

  if type == '1/3_simple':
    fx = body['fx']
    fx = format_fx(fx)
    a = body['a']
    b = body['b']
    data = simpson_13_simple(fx, a, b)
  elif type == '1/3_composite':
    fx = body['fx']
    fx = format_fx(fx)
    a = body['a']
    b = body['b']
    data = simpson_13_composite(fx, a, b, iterations)
  elif type == '3/8_simple':
    fx = body['fx']
    fx = format_fx(fx)
    a = body['a']
    b = body['b']
    data = simpson_38_simple(fx, a, b)
  elif type == '3/8_composite':
    fx = body['fx']
    fx = format_fx(fx)
    a = body['a']
    b = body['b']
    data = simpson_38_composite(fx, a, b, iterations)
  elif type == '1/3_ordered_pairs':
    x = body['x']
    y = body['y']
    data = simpson_pairs_13(x, y)
  elif type == '3/8_ordered_pairs':
    x = body['x']
    y = body['y']
    data = simpson_pairs_38(x, y)
  else:
    fx = body['fx']
    fx = format_fx(fx)
    a = body['a']
    b = body['b']
    data = simpson_13_composite(fx, a, b, iterations)

  res = json.dumps(data)
  return HttpResponse(res, content_type="application/json")
