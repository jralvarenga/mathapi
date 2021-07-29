from django.urls import path

from pages.views import landing_page

# Function
from mathapi.math.function.solve_function import solve_function
from mathapi.math.function.function_points import function_points
from mathapi.math.function.critic_values import function_critic_values

# Derivative
from mathapi.math.derivative.derivative import derivative
from mathapi.math.derivative.derivative_evaluate import derivative_evaluate

# Integral
from mathapi.math.integral.integral import integral
from mathapi.math.integral.integral_evaluate import integral_evaluate

# Gamma Beta function
from mathapi.math.euler_functions.gamma_function import gamma_function
from mathapi.math.euler_functions.beta_function import beta_function
from mathapi.math.euler_functions.phi_function import phi_function

# Ecuation sistem
from mathapi.math.es.gauss_jordan import gauss_jordan
from mathapi.math.es.gauss_seidel import gauss_seidel

# Factorial
from mathapi.math.factorial.factorial import factorial

# Numeric methods
from mathapi.math.methods.function_root.bisection_method import bisection_method
from mathapi.math.methods.function_root.secant_method import secant_method
from mathapi.math.methods.function_root.fixed_point_method import fixed_point_method
from mathapi.math.methods.function_root.false_position import false_position_method
from mathapi.math.methods.function_root.steffensen_method import steffensen_method
from mathapi.math.methods.function_root.newton_rhapson_method import newton_rhapson_method
from mathapi.math.methods.function_root.muller_method import muller_method
from mathapi.math.methods.function_root.halley_method import halley_method

from mathapi.math.methods.integral.trapz_method import trapz_method
from mathapi.math.methods.integral.simpson_method import simpson_method

from mathapi.math.methods.derivative.newton_diference import newton_diference

urlpatterns = [
    path('', landing_page),
    # Function
    path('api/function/solve/', solve_function),
    path('api/function/points/', function_points),
    path('api/function/critic-values/', function_critic_values),
    
    # Derivative
    path('api/derivative/', derivative),
    path('api/derivative/evaluate/', derivative_evaluate),

    # Integral
    path('api/integral/', integral),
    path('api/integral/evaluate/', integral_evaluate),

    # Gamma Beta functions
    path('api/euler-functions/gamma/', gamma_function),
    path('api/euler-functions/beta/', beta_function),
    path('api/euler-functions/phi/', phi_function),

    # Ecuation sistem
    path('api/es/gauss-jordan/', gauss_jordan),
    path('api/es/gauss-seidel/', gauss_seidel),

    # Factorial
    path('api/factorial/', factorial),

    # Numeric methods
    path('api/numeric-methods/function-root/bisection/', bisection_method),
    path('api/numeric-methods/function-root/secant/', secant_method),
    path('api/numeric-methods/function-root/false-position/', false_position_method),
    path('api/numeric-methods/function-root/fixed-point/', fixed_point_method),
    path('api/numeric-methods/function-root/steffensen/', steffensen_method),
    path('api/numeric-methods/function-root/newton-rhapson/', newton_rhapson_method),
    path('api/numeric-methods/function-root/muller/', muller_method),
    path('api/numeric-methods/function-root/halley/', halley_method),
    
    path('api/numeric-methods/integral/trapz/', trapz_method),
    path('api/numeric-methods/integral/simpson/', simpson_method),
    path('api/numeric-methods/derivative/newton-diference/', newton_diference),
]
