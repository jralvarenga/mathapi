import json
import numpy as np

from django.http import HttpResponse

def gauss_jordan(req):
  # Get params
  params = req.GET

  # Get body
  body = json.loads( req.body.decode('utf-8') )
  n = body['unknowns']

  a = np.zeros((n, n + 1))
  x = np.zeros(n)

  for i in range(0, n):
    row = body['row_' + str(i + 1)]
    a[i] = row

  for i in range(n):
    if a[i][i] == 0.0:
      HttpResponse('Error')
        
    for j in range(n):
      if i != j:
        ratio = a[j][i]/a[i][i]

        for k in range(n+1):
          a[j][k] = a[j][k] - ratio * a[i][k]

  for i in range(n):
    x[i] = a[i][n]/a[i][i]

  data = {
    'result': list(x)
  }
  
  res = json.dumps(data)
  return HttpResponse(res, content_type="application/json")