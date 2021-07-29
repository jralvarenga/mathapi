# Function API

> https//mathapi.vercel.app/api/function/

With the functions API you can get the value of a function evaluated in x, the plot pointsof a function or get de critic values (critic points, intervals, concavity & inflexion point) of any f(x) like:

```
f(x) = x^(2) + 3*x + 1
y = e^(x + 1) - 3
g(x) = x^(1/2) + exp(x)
```

The function API is conformed by:

- [Solve Function](#solve-function)
- [Function Points](#function-points)
- [Critic Values](#critic-values)

## Solve function

> With solve function, you receive the value of an function evaluated in c f(c)

### Params

- ?format=many_variables *(optional)* (Solve f(x) in many values given in array)

### Body

```json
{
  "fx": "3*x^(3) + 2*x - 1",
  "value": 3,
  or
  "value": [1, 0.5, 15, 20] (with ?format=many_variables)
}
```

### Request

```bash
curl --request GET \
  'https//mathapi.vercel.app/api/function/solve/' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
      "fx": "3*x^(3) + 2*x - 1",
      "value": 3
    }' \
  --compressed
```

### Response

```json
{
  "result": 86.0
}
```

## Function points

> With function point you get the plot ordered points of a function f(x)

### Params

- ?step=[number] *(optional, default: 1)*

### Body

```json
{
  "fx": "3*x^(3) + 2*x - 1",
  "from": -1,
  "to": 5
}
```

### Request

```bash
curl --request GET \
  'https//mathapi.vercel.app/api/function/points/?step=0.5' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
      "fx": "3*x^(3) + 2*x - 1",
      "from": -1,
      "to": 5
    }' \
  --compressed
```

### Response

```json
{
  "x": [ -1, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0],
  "y": [ -6.0, -2.375, -1.0, 0.375, 4.0, 12.125, 27.0, 50.875, 86.0, 134.625, 199.0, 281.375, 384.0]
}
```

## Critic Values

> With critic values you get the critic point, inflexion point, increase & decrease intervals and concavity of a function f(x)

### Body

```json
{
  "fx": "x^(3) - 3*x^(2) + 2"
}
```

### Request

```bash
curl --request GET \
  'https//mathapi.vercel.app/api/function/critic_values/' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
      "fx": "x^(3) - 3*x^(2) + 2"
    }' \
  --compressed
```

### Response

```json
{
  "critic_points": ["(0.0, 2.0)", "(2.0, -2.0)"],
  "increase_decrease_intervals": [
    {
      "interval": "(-inf, 0)",
      "sign": "+"
    },
    {
      "interval": "(0, 2)",
      "sign": "-"
    },
    {
      "interval": "(2, +inf)",
      "sign": "+"
    }
  ],
  "inflexion_points": ["(1.0, 0.0)"],
  "cocavity": [
    {
      "interval": "(-inf, 1.0)",
      "sign": "-"
    },
    {
      "interval": "(1.0, +inf)",
      "sign": "+"
    }
  ]
}
```