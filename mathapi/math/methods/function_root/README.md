# Function Root

> https//mathapi.vercel.app/api/methods/function-root/

In mathematics, a zero (also sometimes called a root) of a real-, complex-, or generally vector-valued function f, is a member x of the domain of f such that f(x) vanishes at x; that is, the function f attains the value of 0 at x, or equivalently, x is the solution to the equation f(x) = 0. A "zero" of a function is thus an input value that produces an output of 0.

For all the methods listed here the [params](#params) and [response](#response) is the same, only change the body in every method

Methods included:

- [Bisection Method](#bisection-method)
- [False Position](#false-position)
- [Fixed Point](fixed-point)
- [Newton-Rhapson Method](#newton-rhapson-method)
- [Secant Method](#secant-method)
- [Halley's Method](#halley's-method)
- [Muller's Method](#muller's-method)
- [Steffensen's Method](#steffensen's-method)

## Params

- ?tolerancy=[number] *(optional, default: 0, tolerancy for the method in %)*
- ?format=every_iteration *(optional, default: null, show every value finded in every iteration)*

## Bisection method

> https//mathapi.vercel.app/api/methods/function-root/bisection/

The bisection method is a root-finding method that applies to any continuous functions for which one knows two values with opposite signs. The method consists of repeatedly bisecting the interval defined by these values and then selecting the subinterval in which the function changes sign, and therefore must contain a root.

### Body

```json
{
  "fx": "x^(3) - x - 2",
  "a": 1,
  "b": 2
}
```

### Request

```bash
curl --request GET \
  'https//mathapi.vercel.app/api/methods/function-root/bisection/' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
      "fx": "x^(3) - x - 2",
      "a": 1,
      "b": 2
    }' \
  --compressed
```

## Params

- ?tolerancy=[number] *(optional, default: 0, tolerancy for the method in %)*
- ?format=every_iteration *(optional, default: null, show every value finded in every iteration)*

## False Position

> https//mathapi.vercel.app/api/methods/function-root/false-position/

The regula falsi, method of false position, or false position method is a very old method for solving an equation with one unknown; this method, in modified form, is still in use. In simple terms, the method is the trial and error technique of using test ("false") values for the variable and then adjusting the test value according to the outcome

### Body

```json
{
  "fx": "2*x^(3)-2*x-5",
  "xi": 2,
  "xf": 4
}
```

### Request

```bash
curl --request GET \
  'https//mathapi.vercel.app/api/methods/function-root/false-position/' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
      "fx": "2*x^(3)-2*x-5",
      "xi": 2,
      "xf": 4
    }' \
  --compressed
```

## Fixed Point

> https//mathapi.vercel.app/api/methods/function-root/fixed-point/

Fixed-point iteration is a method of computing fixed points of a function. The transcendental equation f(x) = 0 can be converted algebraically into the form x = g(x) and then using the iterative scheme with the recursive relation, for example:

```
f(x) = e^(-x) - x
```

Can be converted to:

```
x = e^(-x)
```
So, the json body for the request would be:

### Body

```json
{
  "fx": "e^(-x)",
  "x0": 1
}
```

### Request

```bash
curl --request GET \
  'https//mathapi.vercel.app/api/methods/function-root/fixed-point/' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
      "fx": "e^(-x)",
      "x0": 1
    }' \
  --compressed
```

## Newton-Rhapson Method

> https//mathapi.vercel.app/api/methods/function-root/newton-rhapson/

Newton's method, also known as the Newton–Raphson method, is a root-finding algorithm which produces successively better approximations to the roots (or zeroes) of a real-valued function

### Body

```json
{
  "fx": "2*x^(3)-2*x-5",
  "xi": 2
}
```

### Request

```bash
curl --request GET \
  'https//mathapi.vercel.app/api/methods/function-root/newton-rhapson/' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
      "fx": "2*x^(3)-2*x-5",
      "xi": 2
    }' \
  --compressed
```

## Secant Method

> https//mathapi.vercel.app/api/methods/function-root/secant/

The secant method is a root-finding algorithm that uses a succession of roots of secant lines to better approximate a root of a function f. The secant method can be thought of as a finite-difference approximation of Newton's method. 

### Body

```json
{
  "fx": "x^(2) - 612",
  "x0": 10,
  "x1": 30
}
```

### Request

```bash
curl --request GET \
  'https//mathapi.vercel.app/api/methods/function-root/secant/' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
      "fx": "x^(2) - 612",
      "x0": 10,
      "x1": 30
    }' \
  --compressed
```

## Halley's Method

> https//mathapi.vercel.app/api/methods/function-root/halley/

Halley's method is a root-finding algorithm used for functions of one real variable with a continuous second derivative.

### Body

```json
{
  "fx": "2*x^(3) - 2*x - 5",
  "xi": 1
}
```

### Request

```bash
curl --request GET \
  'https//mathapi.vercel.app/api/methods/function-root/halley/' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
      "fx": "2*x^(3) - 2*x - 5",
      "xi": 1
    }' \
  --compressed
```

## Muller's Method

> https//mathapi.vercel.app/api/methods/function-root/muller/

Muller's method is a root-finding algorithm, a numerical method for solving equations of the form f(x) = 0.

Muller's method is based on the secant method, which constructs at every iteration a line through two points on the graph of f. Instead, Muller's method uses three points, constructs the parabola through these three points, and takes the intersection of the x-axis with the parabola to be the next approximation.

### Body

```json
{
  "fx": "2*x^(3) - 2*x - 5",
  "x0": 0,
  "x1": 1,
  "x2": 2
}
```

### Request

```bash
curl --request GET \
  'https//mathapi.vercel.app/api/methods/function-root/muller/' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
      "fx": "2*x^(3) - 2*x - 5",
      "x0": 0,
      "x1": 1,
      "x2": 2
    }' \
  --compressed
```

## Steffensen's Method

> https//mathapi.vercel.app/api/methods/function-root/steffensen/

In numerical analysis, Steffensen's method is a root-finding technique named after Johan Frederik Steffensen which is similar to Newton's method. Steffensen's method also achieves quadratic convergence, but without using derivatives as Newton's method does.

### Body

```json
{
  "fx": "2*x^(3)-2*x-5",
  "x0": 1
}
```

### Request

```bash
curl --request GET \
  'https//mathapi.vercel.app/api/methods/function-root/steffensen/' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
      "fx": "2*x^(3)-2*x-5",
      "x0": 1
    }' \
  --compressed
```

## Response

```json
{
  "root": 1.6005987280611713,
  "iterations": 6
}
or (with ?format=every_iteration)
[
  {
    "value": 1.8703703703703705,
    "iteration": 0
  },
  {
    "value": 1.7867391792177618,
    "iteration": 1
  },
  {
    "value": 1.6298280952576243,
    "iteration": 2
  },
  {
    "value": 1.6041158679364038,
    "iteration": 3
  },
  {
    "value": 1.6006711692869842,
    "iteration": 4
  },
  {
    "value": 1.6005987280611713,
    "iteration": 5
  }
]
```