import json
from mathapi.lib.math_ops import evaluate_fx, format_fx
from django.http import HttpResponse

def create_range(start, stop, step):
  arr = [start]
  value = start

  while value < stop:
    value = value + step
    arr.append(value)
  
  return arr


def solve_points(fx, a_limit, b_limit, step):
  x_values = create_range(a_limit, b_limit, step)
  y_values = []

  for x in x_values:
    result = evaluate_fx(fx, x)
    y_values.append(result)

  return {
    'x': x_values,
    'y': y_values
  }


def function_points(req):
  # Get params
  params = req.GET
  step = params.get('step')

  # Get body
  body = json.loads( req.body.decode('utf-8') )
  fx = body['fx']
  
  fx = format_fx(fx)
  from_limit = body['from']
  to_limit = body['to']
  
  if step != None:
    step = float(step)
  else:
    step = 1

  points = solve_points(fx, from_limit, to_limit, step)

  res = json.dumps(points)
  return HttpResponse(res, content_type="application/json")