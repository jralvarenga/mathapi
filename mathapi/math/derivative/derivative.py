import json

from mathapi.lib.math_ops import evaluate_fx, format_fx, format_fx_string, get_dx
from django.http import HttpResponse

def derivative(req):
  # Get params
  params = req.GET
  order = params.get('order')
  order = int(order) if order else 1

  # Get body
  body = json.loads( req.body.decode('utf-8') )
  fx = body['fx']
  fx = format_fx(fx)

  dx = get_dx(fx, order)
  dx = format_fx_string(str(dx))

  data = {
    'derivative': dx,
    'order': order
  }

  res = json.dumps(data)
  return HttpResponse(res, content_type="application/json")