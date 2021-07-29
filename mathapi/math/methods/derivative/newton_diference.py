import json

from mathapi.lib.math_ops import absolute_error, evaluate_fx, format_fx
from django.http import HttpResponse

# Diferentation foward O(h)
def forward_method(fx, x, h, order):
  x_i = x
  x_i1 = x + h
  x_i2 = x + 2*h
  x_i3 = x + 3*h
  x_i4 = x + 4*h

  y_i = evaluate_fx(fx, x_i)
  y_i1 = evaluate_fx(fx, x_i1)
  y_i2 = evaluate_fx(fx, x_i2)
  y_i3 = evaluate_fx(fx, x_i3)
  y_i4 = evaluate_fx(fx, x_i4)

  if order == 1:
    value = (y_i1 - y_i)/(h)
  elif order == 2:
    value = (y_i2 - 2*y_i1 + y_i)/(h**(2))
  elif order == 3:
    value = (y_i3 - 3*y_i2 + 3*y_i1 - y_i)/((h**(3))*3)
  elif order == 4:
    value = (y_i4 - 4*y_i3 + 6*y_i2 - 4*y_i1 + y_i)/(h**(4))

  return {
    'derivative': value
  }

# Diferentation foward O(h2)
def forward_method_oh2(fx, x, h, order):
  x_i = x
  x_i1 = x + h
  x_i2 = x + 2*h
  x_i3 = x + 3*h
  x_i4 = x + 4*h
  x_i5 = x + 5*h

  y_i = evaluate_fx(fx, x_i)
  y_i1 = evaluate_fx(fx, x_i1)
  y_i2 = evaluate_fx(fx, x_i2)
  y_i3 = evaluate_fx(fx, x_i3)
  y_i4 = evaluate_fx(fx, x_i4)
  y_i5 = evaluate_fx(fx, x_i5)

  if order == 1:
    value = (-y_i2 + 4*y_i1 - 3*y_i)/(2*h)
  elif order == 2:
    value = (-y_i3 + 4*y_i2 - 5*y_i1 + 2*y_i)/(h**(2))
  elif order == 3:
    value = (-3*y_i4 + 14*y_i3 - 24*y_i2 + 18*y_i1 - 5*y_i)/(2*h**(3))
  elif order == 4:
    value = (-2*y_i5 + 11*y_i4 - 24*y_i3 + 26*y_i2 - 14*y_i1 + 3*y_i)/(h**(4))

  return {
    'derivative': value
  }

# Diferentation backward O(h)
def backward_method(fx, x, h, order):
  x_i = x
  x_i1 = x - h
  x_i2 = x - 2*h
  x_i3 = x - 3*h
  x_i4 = x - 4*h

  y_i = evaluate_fx(fx, x_i)
  y_i1 = evaluate_fx(fx, x_i1)
  y_i2 = evaluate_fx(fx, x_i2)
  y_i3 = evaluate_fx(fx, x_i3)
  y_i4 = evaluate_fx(fx, x_i4)

  if order == 1:
    value = (y_i - y_i1)/(h)
  elif order == 2:
    value = (y_i - 2*y_i1 + y_i2)/(h**(2))
  elif order == 3:
    value = (y_i - 3*y_i1 + 3*y_i2 - y_i3)/(2*h**(3))
  elif order == 4:
    value = (y_i - 4*y_i1 + 6*y_i2 - 4*y_i3 + y_i4)/(h**(4))

  return {
    'derivative': value
  }

# Diferentation backward O(h2)
def backward_method_oh2(fx, x, h, order):
  x_i = x
  x_i1 = x - h
  x_i2 = x - 2*h
  x_i3 = x - 3*h
  x_i4 = x - 4*h
  x_i5 = x - 5*h

  y_i = evaluate_fx(fx, x_i)
  y_i1 = evaluate_fx(fx, x_i1)
  y_i2 = evaluate_fx(fx, x_i2)
  y_i3 = evaluate_fx(fx, x_i3)
  y_i4 = evaluate_fx(fx, x_i4)
  y_i5 = evaluate_fx(fx, x_i5)

  if order == 1:
    value = (3*y_i - 4*y_i1 + y_i2)/(2*h)
  elif order == 2:
    value = (2*y_i - 5*y_i1 + 4*y_i2 - y_i3)/(h**(2))
  elif order == 3:
    value = (5*y_i - 18*y_i1 + 24*y_i2 - 14*y_i3 + 3*y_i4)/(2*h**(3))
  elif order == 4:
    value = (3*y_i - 14*y_i1 + 26*y_i2 - 24*y_i3 + 11*y_i4 - 2*y_i5)/(h**(4))

  return {
    'derivative': value
  }

# Diferentation divided O(h)
def divided_method(fx, x, h, order):
  x_i = x
  x_i1 = x + h
  x_i2 = x + 2*h
  x_1i = x - h
  x_2i = x - 2*h

  y_i = evaluate_fx(fx, x_i)
  y_i1 = evaluate_fx(fx, x_i1)
  y_i2 = evaluate_fx(fx, x_i2)
  y_1i = evaluate_fx(fx, x_1i)
  y_2i = evaluate_fx(fx, x_2i)

  if order == 1:
    value = (y_i1 - y_1i)/(2*h)
  elif order == 2:
    value = (y_i1 - 2*y_i + y_1i)/(h**(2))
  elif order == 3:
    value = (y_i2 - 2*y_i1 + 2*y_1i - y_2i)/(2*h**(3))
  elif order == 4:
    value = (y_i2 - 4*y_i1 + 6*y_i - 4*y_1i + y_2i)/(h**(4))

  return {
    'derivative': value
  }

# Diferentation divided O(h2)
def divided_method_oh2(fx, x, h, order):
  x_i = x
  x_i1 = x + h
  x_i2 = x + 2*h
  x_i3 = x + 3*h
  x_1i = x - h
  x_2i = x - 2*h
  x_3i = x - 3*h

  y_i = evaluate_fx(fx, x_i)
  y_i1 = evaluate_fx(fx, x_i1)
  y_i2 = evaluate_fx(fx, x_i2)
  y_i3 = evaluate_fx(fx, x_i3)
  y_1i = evaluate_fx(fx, x_1i)
  y_2i = evaluate_fx(fx, x_2i)
  y_3i = evaluate_fx(fx, x_3i)

  if order == 1:
    value = (-y_i2 + 8*y_i1 - 8*y_1i + y_2i)/(12*h)
  elif order == 2:
    value = (-y_i2 + 16*y_i1 - 30*y_i + 16*y_1i - y_2i)/(12*h**(2))
  elif order == 3:
    value = (-y_i3 + 8*y_i2 - 13*y_i1 + 13*y_1i - 8*y_2i + y_3i)/(8*h**(3))
  elif order == 4:
    value = (-y_i3 + 12*y_i2 - 39*y_i1 + 56*y_i - 39*y_1i + 12*y_2i - y_3i)/(6*h**(4))

  return {
    'derivative': value
  }

def newton_diference(req):
  # Get params
  params = req.GET
  type = params.get('type')
  order = int(params.get('order')) if params.get('order') != None else 1

  # Get body
  body = json.loads( req.body.decode('utf-8') )
  fx = body['fx']
  fx = format_fx(fx)
  x = body['x']
  h = body['h']

  if type == 'forward' or type == 'forward_oh':
    data = forward_method(fx, x, h, order)
  if type == 'forward_oh2':
    data = forward_method_oh2(fx, x, h, order)
  if type == 'backward' or type == 'backward_oh':
    data = backward_method(fx, x, h, order)
  if type == 'backward_oh2':
    data = backward_method_oh2(fx, x, h, order)
  if type == 'divided' or type == 'divided_oh':
    data = divided_method(fx, x, h, order)
  if type == 'divided_oh2':
    data = backward_method_oh2(fx, x, h, order)
  else:
    data = divided_method(fx, x, h, order)

  res = json.dumps(data)
  return HttpResponse(res, content_type="application/json")
