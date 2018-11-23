# Comments(댓글)

## 댓글 생성하기

**Request**:

`POST` `api/v1/articles/:slug/comments`
```json
Content-Type application/json
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

{
  "comment": {
    "body": "I think you need him to go through abdominal CT first, and THEN decide what to do."
  }
}
```

**Response**:

```json
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept 

{
    "id": "a9c442fe-5585-4dbf-abed-2b3bec6a0642",
    "author": {
        "username": "admin",
        "bio": "",
        "image": "https://static.productionready.io/images/smiley-cyrus.jpg",
        "following": false
    },
    "body": "I think you need him to go through abdominal CT first, and THEN decide what to do.",
    "created": "now",
    "modified": "now"
}
```

## 특정 질문(=article)에 대한 댓글들 가져오기

**Request**:

`GET` `api/v1/articles/:slug/comments`
```json
Content-Type application/json
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

**Response**:

```json
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "26a9762e-af6d-41a4-a97c-e5be6d262f7b",
            "author": {
                "username": "test",
                "bio": "",
                "image": "https://static.productionready.io/images/smiley-cyrus.jpg",
                "following": false
            },
            "body": "I think you need him to go through abdominal CT first, and THEN decide what to do.",
            "created": "6 seconds ago",
            "modified": "6 seconds ago"
        },
        {
            "id": "3193f8a3-d0df-4060-a642-eb14cb84c0c6",
            "author": {
                "username": "test",
                "bio": "",
                "image": "https://static.productionready.io/images/smiley-cyrus.jpg",
                "following": false
            },
            "body": "I think you need him to go through abdominal CT first, and THEN decide what to do.",
            "created": "9 seconds ago",
            "modified": "9 seconds ago"
        }
    ]
}
```

## 질문 detail 가져오기

**Request**:

`GET` `api/v1/articles/:slug`
```json
Content-Type application/json
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

**Response**:

```json
HTTP 200 OK
Allow: GET, PUT, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "author": {
        "username": "admin",
        "bio": "",
        "image": "https://static.productionready.io/images/smiley-cyrus.jpg",
        "following": false
    },
    "body": "57세 남자 환자가 오늘 내원해서 5달간 지속된 황달과 피로 증상을 호소하는데요, 어떤 처방을 주면 좋을까요??",
    "created": "7 minutes ago",
    "description": "황달 환자 처방 최신 경향",
    "favorited": false,
    "favoritesCount": 0,
    "slug": "-a1xnnn",
    "tagList": [
        "소화기내과",
        "암",
        "췌장"
    ],
    "title": "황달있는 환자에게 뭘 처방해야 하나요?",
    "modified": "7 minutes ago"
}
```
