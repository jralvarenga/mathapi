import json

from mathapi.lib.math_ops import evaluate_fx, format_fx
from django.http import HttpResponse

def solve_fx_handler(fx, x):
  result = evaluate_fx(fx, x)
  return {
    'result': result
  }

def solve_with_many_variables(fx, values):
  results = map(lambda x: evaluate_fx(fx, x), values)
  return {
    'result': list(results),
  }

def solve_function(req):
  # Get params
  params = req.GET
  format = params.get('format')

  # Get body
  body = json.loads( req.body.decode('utf-8') )
  fx = body['fx']
  
  fx = format_fx(fx)

  if format == 'many_variables':
    # Solves with array of values
    variable_values = body['value']
    response = solve_with_many_variables(fx, variable_values)
  else:
    # Solves with one value
    variable_value = body['value']
    response = solve_fx_handler(fx, variable_value)

  res = json.dumps(response)
  return HttpResponse(res, content_type="application/json")