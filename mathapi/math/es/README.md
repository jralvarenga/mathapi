# Ecuation Sistem API

> https//mathapi.vercel.app/api/es/

With the ES API you get the solution for any ecuation sistem like:

```
x + y + z = 2
5*x/3 + 6*z - 2*y = 0
2*x - y - z = -1
```

This API is conformed by:

- [Gauss-Jordan Method](#gauss-jordan-method)
- [Gauss-Seidel Method](#gauss-seidel-method)

## Gauss-Jordan Method

> With this method you get the solution of any ecuation sistem of n variables

### Body

The ecuation sistem:

```
x + y + z + q = 11
2x - 3y + 4z - 1q = 15
3x + 4y - 5z + 2q = 40,
3x + 4y - 5z + 5q = 0
```

Is ecual to the json body:

```json
{
  "unknowns": 4,
  "row_1": [1, 1, 1, 2, 11],
  "row_2": [2, -3, 4, -1, 15],
  "row_3": [3, 4, 5, 2, 40],
  "row_4": [3, 4, 5, 5, 0]
}
```
**For more variables add the number of unknowns into `"unknowns": n` and add `"row_n": []` as many has it needs**

### Request

```bash
curl --request GET \
  'https//https//mathapi.vercel.app/api/es/gauss-jordan/' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
      "unknowns": 4,
      "row_1": [1, 1, 1, 2, 11],
      "row_2": [2, -3, 4, -1, 15],
      "row_3": [3, 4, 5, 2, 40],
      "row_4": [3, 4, 5, 5, 0]
    }' \
  --compressed
```

### Response

```json
{
  "result": [58.556, 4.555, -25.4446, -13.333334 ]
}
```

## Gauss-Seidel Method

> With this method you get the solution for x, y & z in a 3 unknowns ecuartion sistem

### Params

- ?error=[number] *(optional, defualt: 0, tolerancy for the method in %)*

### Body

Each of the variables needs to be cleared for the 3 ecuations, for example, the ecuation sistem:

```
x + y + z = 1
2x + 3y - z = 0
x/2 - z + y = -1
```

Would be ecual to:

```
x = 1 - y - z
y = (-2x + z)/3
z = 1 + x/2 + y
```

And the json body would be:

```json
{
  "fx": "1 - y - z",
  "fy": "(-2*x + z)/3",
  "fz": "1 + x/2 + y"
}
```

### Request

```bash
curl --request GET \
  'https//https//mathapi.vercel.app/api/es/gauss-seidel/' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
      "fx": "1 - y - z",
      "fy": "(-2*x + z)/3",
      "fz": "1 + x/2 + y"
    }' \
  --compressed
```

### Response

```json
{
  "x": "1",
  "y": "0.0",
  "z": "1.0"
}
```