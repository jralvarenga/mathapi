# Derivative API

> https//mathapi.vercel.app/api/derivative/

With the derivative API you get the derivative of a function f(x) or you can get that derivative evaluated in a point c given

Function examples:

```
f(x) = 3*x^(3) - 2*x^(1/2) + 1
y = e^(x)
g(x) = sqrt(x) + exp(x)
```

The derivative API is conformed by:

- [Function Derivative](#function-derivative)
- [Evaluate derivative](#evaluate-derivative)

## Function Derivative

> With function derivative you get the derivative order n of an f(x) given

### Params

- ?order=[number] *(optional, default: 1)*

### Body

```json
{
  "fx": "3*x^(3) - 2*x^(1/2) + 1"
}
```
### Request

```bash
curl --request GET \
  'https//https//mathapi.vercel.app/api/derivative' \
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
  "derivative": "9*x^2 - 1/sqrt(x)",
  "order": 1
}
```

## Evaluate derivative

> With evaluate derivative you get the derivative order n for any f(x) and evalutated in any c point given

### Params

- ?order=[number] *(optional, default: 1)*

### Body

```json
{
  "fx": "3*x^(3) - 2*x^(1/2) + 1",
  "x": 3
}
```
### Request

```bash
curl --request GET \
  'https//https//mathapi.vercel.app/api/derivative/evaluate/' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
      "fx": "3*x^(3) - 2*x^(1/2) + 1",
      "x": 3
    }' \
  --compressed
```

### Response

```json
{
  "derivative": 80.42264973081038,
  "order": 1
}
```