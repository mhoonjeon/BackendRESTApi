# Tags(태그)

## 태그 팔로우하기

**request**:

`POST` `api/v1/tags/:tagname/follow`
```json
content-type application/json
authorization: token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

**response**:

```json
HTTP 200 OK
Allow: POST, DELETE, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "username": "admin",
    "bio": "",
    "image": "https://static.productionready.io/images/smiley-cyrus.jpg",
    "following": false,
    "following_tag": false  // true 일수도 있고 false 일수도 있다. 단지 유저가 팔로우하고 있는 tag가 한개라도 있는지
    확인하는 필드
}
```

## 태그 언팔로우하기

**request**:

`DELETE` `api/v1/tags/:tagname/follow`
```json
content-type application/json
authorization: token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```
**query parameter(선택사항)**:

**response**:

```json
http 201 created
allow: post, delete, options
content-type: application/json
vary: accept

{
    "username": "admin",
    "bio": "",
    "image": "https://static.productionready.io/images/smiley-cyrus.jpg",
    "following": false,
    "following_tag": true
}
```

## 태그 가져오기

**Request**:

`GET` `api/v1/tags`
```json
Content-Type application/json
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```
**Query Parameter(선택사항)**:

* `GET` `api/v1/tags/?followed=admin`: 특정 유저가 팔로우하고 있는 태그만 가져오기(Username으로 필터)

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
