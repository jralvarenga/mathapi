import json

from mathapi.lib.math_ops import format_fx, format_fx_string, get_integral_fx
from django.http import HttpResponse

def integral(req):
  # Get params
  params = req.GET
  order = params.get('order')
  order = int(order) if order else 1

  # Get body
  body = json.loads( req.body.decode('utf-8') )
  fx = body['fx']
  fx = format_fx(fx)

  integral = get_integral_fx(fx)
  integral = format_fx_string(str(integral))

  data = {
    'integral': integral,
  }

  res = json.dumps(data)
  return HttpResponse(res, content_type="application/json")