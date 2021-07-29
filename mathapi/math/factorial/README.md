# Factorial API

> https//mathapi.vercel.app/api/factorial/

With the factorial API you get the result of the factorial of any integer or fraction number

### Body

```json
{
  "n": "1/2"
}
```
### Request

```bash
curl --request GET \
  'https//https//mathapi.vercel.app/api/factorial/' \
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
  "factorial": 0.886226925452758
}
```