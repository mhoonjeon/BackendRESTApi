# Tags(태그)

## 태그 가져오기

**Request**:

`GET` `api/v1/tags`
```json
Content-Type application/json
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

**Response**:

```json
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "tags": [
        "testtag",
        "소화기내과",
        "암",
        "췌장",
        "Gastrointestinal",
        "Cancer",
        "Pancrease"
    ]
}
```
