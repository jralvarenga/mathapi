import json
import re

from mathapi.lib.math_ops import evaluate_fx, format_fx, get_dx, solve_function
from django.http import HttpResponse

############### Gets increase and decrease intervals and x values of critic points
def get_critic_intervals(dx):

  def define_limits(limits):
    defined = ['(-inf, '+ str(limits[0]) + ')']

    if len(limits) == 1:
      defined.append('('+ str(limits[0]) + ', +inf)')
      return defined

    if (len(limits) % 2) == 0:
      step = 2
    else:
      step = 1

    for i in range(0, len(limits), step):
      limit = '(' + str(limits[i]) + ', ' + str(limits[i + 1]) + ')'
      defined.append(limit)
      if step == 1 & i : break
    
    defined.append('('+ str(limits[-1]) + ', +inf)')

    return defined

  def define_limits_with_sign(limits, signs):
    values = []
    for i in range(0, len(limits)):
      values.append({
        'interval': limits[i],
        'sign': signs[i]
      })
    return values

  def value_sign(values):
    data = []
    for i in range(0, len(values)):
      sign = '+' if values[i] >= 0 else '-'
      data.append(sign)
      
    return data

  def get_values(limits):
    values = []
    for i, x in enumerate(limits):
      vl = evaluate_fx(str(dx), x - 1)
      values.append(vl)
      if i:
        vl2 = evaluate_fx(str(dx), x + 1)
        values.append(vl2)
    return values
  
  has_x = re.search('x', str(dx))
  if has_x:
    sympy_values = solve_function(dx)
    limit_values = list(sympy_values)
    values = get_values(limit_values)
    signs = value_sign(values)
    defined_limits = define_limits(limit_values)
    limits_with_sign = define_limits_with_sign(defined_limits, signs)
    
    critic_points = []
    for i, point in enumerate(limit_values):
      critic_points.append(float(point))
    
    data = {
      'critic_points': critic_points,
      'limits': limits_with_sign
    }

    return data
  else:
    return None

############### Gets inflexion point
def define_critic_points(fx, points):
  values = []
  for x in points:
    y = evaluate_fx(fx, x)
    point = '(' + str(x) + ', ' + str(y) + ')'
    values.append(point)

  return values

############### Gets inflexion point
def get_inflexion_points(dx):
  has_x = re.search('x', str(dx))
  if has_x:
    sympy_values = solve_function(dx)
    x_values = []

    for i, x in enumerate(list(sympy_values)):
      x_values.append(float(x))

    data = {
      'inflexion_points': x_values
    }

    return data
  else:
    return None

############### Gets inflexion point
def define_inflexion_points(fx, points):
  values = []
  for x in points:
    y = evaluate_fx(fx, x)
    point = '(' + str(x) + ', ' + str(y) + ')'
    values.append(point)

  return values

############### Gets function concavity
def get_concavity(dx, inflexion_points, critic_points):

  def define_limits(limits):
    defined = ['(-inf, '+ str(limits[0]) + ')']

    if len(limits) == 1:
      defined.append('('+ str(limits[0]) + ', +inf)')
      return defined

    if (len(limits) % 2) == 0:
      step = 2
    else:
      step = 1

    for i in range(0, len(limits), step):
      limit = '(' + str(limits[i]) + ', ' + str(limits[i + 1]) + ')'
      defined.append(limit)
      if step == 1 & i : break
    
    defined.append('('+ str(limits[-1]) + ', +inf)')

    return defined

  def evaluate_in_critic_points(dx, points):
    values = []
    for x in points:
      vl = evaluate_fx(str(dx), x)
      values.append(vl)

    return values

  def define_concavity(values, limits):
    values = []
    for i in range(0, len(limits)):
      values.append({
        'interval': limits[i],
        'sign': signs[i]
      })
    return values

  def value_sign(values):
    data = []
    for i in range(0, len(values)):
      sign = '+' if values[i] >= 0 else '-'
      data.append(sign)
      
    return data

  has_x = re.search('x', str(dx))
  if has_x:
    values = evaluate_in_critic_points(dx, critic_points)
    signs = value_sign(values)
    limits = define_limits(inflexion_points)
    defined = define_concavity(signs, limits)

    data = {
      'concavity': defined
    }

    return data
  else:
    return None

###########################################

def function_critic_values(req):
  # Get body
  body = json.loads( req.body.decode('utf-8') )
  fx = body['fx']
  
  fx = format_fx(fx)
  d1x = get_dx(fx, 1)
  d2x = get_dx(fx, 2)

  critic_intervals = get_critic_intervals(d1x)
  critic_points = define_critic_points(fx, critic_intervals['critic_points'])
  increaseDecrease_intervals = critic_intervals['limits']
  inflexion_x_points = get_inflexion_points(d2x)
  inflexion_points = define_inflexion_points(fx, inflexion_x_points['inflexion_points'])
  concavity = get_concavity(d2x, inflexion_x_points['inflexion_points'], critic_intervals['critic_points'])

  data = {
    'critic_points': critic_points,
    'increase_decrease_intervals': increaseDecrease_intervals,
    'inflexion_points': inflexion_points,
    'cocavity': concavity['concavity']
  }

  res = json.dumps(data)
  return HttpResponse(res, content_type="application/json")