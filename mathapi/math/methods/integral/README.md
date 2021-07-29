# Integral Value Methods

> https//mathapi.vercel.app/api/methods/integral/

An integral assigns numbers to functions in a way that describes displacement, area, volume, and other concepts that arise by combining infinitesimal data. The process of finding integrals is called integration. Along with differentiation, integration is a fundamental, essential operation of calculus, and serves as a tool to solve problems in mathematics and physics involving the area of an arbitrary shape, the length of a curve, and the volume of a solid, among others.

For all the methods listed here the  [response](#response) is the same, only change the params & body in every method

Methods included:

- [Trapezoidal Rule](#trapezoidal-rule)
- [Simpson's Method](#simpson's-method)

## Trapezoidal Rule

The trapezoidal rule (also known as the trapezoid rule or trapezium rule—see Trapezoid for more information on terminology) is a technique for approximating the definite integral. The trapezoidal rule works by approximating the region under the graph of the function f(x) as a trapezoid and calculating its area

### Params

- `?iterations=[number]` *(optional, default: 100, Number of iterations to be done)*
- `?type=simple | composite | ordered_pairs` *(optional, default: composite, Type of trapz rule to do)*

### Body

```json
{
  "fx": "3*x^(2) + 3*x - 1",
  "a": 0,
  "b": 1
}
or (with ?type=ordered_pairs)
{
  "x": [1.4, 1.6, 1.8, 2, 2.2],
  "y": [4.0552, 4.953, 6.0436, 7.3891, 9.025]
}
```

### Request

```bash
curl --request GET \
  'https//mathapi.vercel.app/api/methods/integral/trapz/' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
      "fx": "3*x^(2) + 3*x - 1",
      "a": 0,
      "b": 1
    }' \
  --compressed
```

## Simpson's Method

Simpson's rules are several approximations for definite integrals. The most basic of these rules is called Simpson's 1/3 rule, or just Simpson's rule

If the 1/3 rule is applied to n equal subdivisions of the integration range [a, b], one obtains the composite Simpson's rule. Points inside the integration range are given alternating weights 4/3 and 2/3.

Simpson's 3/8 rule, also called Simpson's second rule requires one more function evaluation inside the integration range and gives lower error bounds, but does not improve on order of the error.

Simpson's 1/3 and 3/8 rules are two special cases of closed Newton–Cotes formulas.

### Params

- `?iterations=[number]` *(optional, default: 100, Number of iterations to be done)*
- `?type=1/3_simple | 1/3_composite | 3/8_simple | 3/8_composite | 1/3_ordered_pairs | 3/8_ordered_pairs` *(optional, default: simpson_13_composite, Type of simspon's rule to do)*

### Body

```json
{
  "fx": "3*x^(2) + 3*x - 1",
  "a": 0,
  "b": 1
}
or (with ?type=ordered_pairs)
{
  "x": [1.4, 1.6, 1.8, 2, 2.2],
  "y": [4.0552, 4.953, 6.0436, 7.3891, 9.025]
}
```

### Request

```bash
curl --request GET \
  'https//mathapi.vercel.app/api/methods/integral/simpson/' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
      "fx": "3*x^(2) + 3*x - 1",
      "a": 0,
      "b": 1
    }' \
  --compressed
```

## Response

```json
{
  "integral": 0.6931471808723674,
  "error": 0.0
}
```