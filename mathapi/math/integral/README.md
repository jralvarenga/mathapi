# integral API

> https//mathapi.vercel.app/api/integral

With the integral API you get the integral of a function f(x) or you can get that integral evaluated in a point c given

Function examples:

```
f(x) = 3*x^(3) - 2*x^(1/2) + 1
y = e^(x)
g(x) = sqrt(x) + exp(x)
```

The integral API is conformed by:

- [Function integral](#function-integral)
- [Evaluate integral](#evaluate-integral)

## Function Integral

> With function integral you get the integral of an f(x) given

### Body

```json
{
  "fx": "3*x^(3) - 2*x^(1/2) + 1"
}
```
### Request

```bash
curl --request GET \
  'https//https//mathapi.vercel.app/api/integral/' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
      "fx": "3*x^(3) - 2*x^(1/2) + 1"
    }' \
  --compressed
```

### Response

```json
{
  "integral": "-4*x^(3/2)/3 + 3*x^4/4 + x"
}
```

## Evaluate Integral

> With evaluate integral you get the integral for any f(x) and evalutated in an interval [a, b] given

### Body

```json
{
  "fx": "3*x^(3) - 2*x^(1/2) + 1",
  "a": 1,
  "b": 5,
  or
  "a": 0,
  "b": "inf",
  or
  "a": "a",
  "b": "b"
}
```
### Request

```bash
curl --request GET \
  'https//https//mathapi.vercel.app/api/integral/evaluate/' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
      "fx": "3*x^(3) - 2*x^(1/2) + 1",
      "a": 1,
      "b": 5
    }' \
  --compressed
```

### Response

```json
{
  "integral": "556/3",
  or
  "integral": "-4*a^(3/2)/3 + 3*a^4/4 + a"
}
```