# Numerical Differentiation Methods

> https//mathapi.vercel.app/api/methods/derivative/

Numerical differentiation is the process of finding the numerical value of a derivative of a given function at a given point. In general, numerical differentiation is more difficult than numerical integration. This is because while numerical integration requires only good continuity properties of the function being integrated, numerical differentiation requires more complicated properties such as Lipschitz classes.

For all the methods listed here the  [response](#response) is the same, only change the params & body in every method

Methods included:

- [Finite Difference or Newton Differeces](#finite-difference)

## Finite Difference

A finite difference, also known as Newton Differeces is a mathematical expression of the form f(x + b) − f(x + a). If a finite difference is divided by b − a, one gets a difference quotient. The approximation of derivatives by finite differences plays a central role in finite difference methods for the numerical solution of differential equations, especially boundary value problems.

### Params

- `?type=forward | forward_oh | forward_oh2 | backward | backward_oh | backward_oh2 | divided | divided_oh | divided_oh2` *(optional, default: divided_oh, Type of Finite difference to do)*
- order=[number] *(optional, defualt: 1, Derivative order to find)*

### Body

```json
{
  "fx": "-0.1*x^(4) - 0.15*x^(3) - 0.5*x^(2) - 0.25*x + 1.2",
  "x": 0.5,
  "h": 0.5
}
```
### Request

```bash
curl --request GET \
  'https//mathapi.vercel.app/api/methods/derivative/simpson/newton-diference/' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
      "fx": "-0.1*x^(4) - 0.15*x^(3) - 0.5*x^(2) - 0.25*x + 1.2",
      "x": 0.5,
      "h": 0.5
    }' \
  --compressed
```

### Response

```json
{
  "derivative": -1.0
}
```