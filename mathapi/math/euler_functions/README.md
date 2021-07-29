# Euler Functions API

> https//mathapi.vercel.app/api/euler-functions/

With Euler functions API you can get the Gamma function, Beta function or Phi function of any number given

The API is conformed by

- [Gamma Function](#gamma-function)
- [Beta Function](#beta-function)
- [Phi Function](#phi-function)

## Gamma function

> With Gamma function API you get the gamma function of a number given

### Body

```json
{
  "n": "1/2"
}
```
### Request

```bash
curl --request GET \
  'https//https//mathapi.vercel.app/api/euler-functions/gamma/' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
      "n": "1/2"
    }' \
  --compressed
```

### Response

```json
{
  "gamma": 1.772453850905516
}
```

## Beta function

> With Beta function API you get the beta function of a (x, y) point given

### Body

```json
{
  "x": "1/2",
  "y": "3"
}
```
### Request

```bash
curl --request GET \
  'https//https//mathapi.vercel.app/api/euler-functions/beta/' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
      "x": "1/2",
      "y": "3"
    }' \
  --compressed
```

### Response

```json
{
  "beta": 1.0666666666666667
}
```

## Phi function

> With Phi function API you get the phi function of an integer number given

### Body

```json
{
  "n": 15,
}
```
### Request

```bash
curl --request GET \
  'https//https//mathapi.vercel.app/api/euler-functions/phi/' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  --data '{
      "n": 15
    }' \
  --compressed
```

### Response

```json
{
  "phi": 8.0
}
```