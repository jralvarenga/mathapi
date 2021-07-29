import json

from sympy import *
from mathapi.lib.math_ops import absolute_error
from django.http import HttpResponse

def gauss_seidel(req):
  # Get params
  params = req.GET
  tolerancy = params.get('error')

  if tolerancy != None:
    tolerancy = float(tolerancy) / 100
  else:
    tolerancy = 0

  # Get body
  body = json.loads( req.body.decode('utf-8') )
  fx = body['fx']
  fy = body['fy']
  fz = body['fz']

  f1 = lambda x,y,z: eval(fx)
  f2 = lambda x,y,z: eval(fy)
  f3 = lambda x,y,z: eval(fz)

  xi = 0
  yi = 0
  zi = 0
  k = 0
  loop = True

  while loop:
    x1 = f1(xi, yi, zi)
    y1 = f2(xi, yi, zi)
    z1 = f3(xi, yi, zi)

    e1 = absolute_error(xi, x1)
    e2 = absolute_error(yi, y1)
    e3 = absolute_error(zi, z1)

    xi, yi, zi = x1, y1, z1
    k = k + 1
    loop = e1 > tolerancy and e2 > tolerancy and e3 > tolerancy

  data = {
    'x': str(x1),
    'y': str(y1),
    'z': str(z1)
  }

  res = json.dumps(data)
  return HttpResponse(res, content_type="application/json")