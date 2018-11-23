# Articles(Questions)

## 질문(article) 생성하기

**Request**:

`PtST` `api/v1/articles/`
```json
Content-Type application/json
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

{
  "article": {
    "title": "What medication should I prescribe to patient with jaundice?",
    "description": "Dealing with patient with possible pancreatic head cancer",
    "body": "A 57-year-old male patient came to my clinic today, complaing about jaundice and malaise that existed for the last 5 months. What kind of medication should I give him?",
    "tagList": ["Pancrease", "Cancer", "Gastrointestinal"]
  }
}
```

**Parameters**:

Name       | 설명      | 타입   | 필수 | 주의
-----------|-----------|--------|------|------------
title      | 제목      | string | Yes  |
description| 요약?     | string | Yes  | 
body       | 본문      | string | Yes  | 
tagList    | 태그      |        | No   | 

**Response**:

```json
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept 

{
    "author": {
        "username": "admin",
        "bio": "",
        "image": "https://static.productionready.io/images/smiley-cyrus.jpg",
        "following": false
    },
    "body": "A 57-year-old male patient came to my clinic today, complaing about jaundice and malaise that existed for the last 5 months. What kind of medication should I give him?",
    "created": "now",
    "description": "Dealing with patient with possible pancreatic head cancer",
    "favorited": false,
    "favoritesCount": 0,
    "slug": "what-medication-should-i-prescribe-to-patient-with-jaundice-0adb2r",
    "tagList": [
        "Gastrointestinal",
        "Cancer",
        "Pancrease"
    ],
    "title": "What medication should I prescribe to patient with jaundice?",
    "modified": "now"
}
```

## 질문 리스트 가져오기

**Request**:

`GET` `api/v1/articles/`
```json
Content-Type application/json
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```
**Query Parameter(선택사항)**:

* `GET` `api/v1/charts/?tag=Pancrease`: 태그로 필터링  
* `GET` `api/v1/charts/?author=admin`:  작성자로 필터링  
* `GET` `api/v1/charts/?favorited=admin`: 좋아요로 필터링 (좋아요 누른 사람의 feed 보여주기 위해)

**Response**:

```json
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 5,
    "next": null,
    "previous": "http://localhost:8000/api/v1/articles/",
    "results": [
        {
            "author": {
                "username": "admin",
                "bio": "",
                "image": "https://static.productionready.io/images/smiley-cyrus.jpg",
                "following": false
            },
            "body": "57세 남자 환자가 오늘 내원해서 5달간 지속된 황달과 피로 증상을 호소하는데요, 어떤 처방을 주면 좋을까요??",
            "created": "43 minutes ago",
            "description": "황달 환자 처방 최신 경향",
            "favorited": false,
            "favoritesCount": 0,
            "slug": "-30p7rp",
            "tagList": [
                "소화기내과",
                "암",
                "췌장"
            ],
            "title": "황달있는 환자에게 뭘 처방해야 하나요?",
            "modified": "43 minutes ago"
        },
        {
            "author": {
                "username": "admin",
                "bio": "",
                "image": "https://static.productionready.io/images/smiley-cyrus.jpg",
                "following": false
            },
            "body": "57세 남자 환자가 오늘 내원해서 5달간 지속된 황달과 피로 증상을 호소하는데요, 어떤 처방을 주면 좋을까요??",
            "created": "43 minutes ago",
            "description": "황달 환자 처방 최신 경향",
            "favorited": false,
            "favoritesCount": 0,
            "slug": "-d9nxwv",
            "tagList": [
                "소화기내과",
                "암",
                "췌장"
            ],
            "title": "황달있는 환자에게 뭘 처방해야 하나요?",
            "modified": "43 minutes ago"
        },
        {
            "author": {
                "username": "admin",
                "bio": "",
                "image": "https://static.productionready.io/images/smiley-cyrus.jpg",
                "following": false
            },
            "body": "57세 남자 환자가 오늘 내원해서 5달간 지속된 황달과 피로 증상을 호소하는데요, 어떤 처방을 주면 좋을까요??",
            "created": "43 minutes ago",
            "description": "황달 환자 처방 최신 경향",
            "favorited": false,
            "favoritesCount": 0,
            "slug": "-fq05er",
            "tagList": [
                "소화기내과",
                "암",
                "췌장"
            ],
            "title": "황달있는 환자에게 뭘 처방해야 하나요?",
            "modified": "43 minutes ago"
        },
        {
            "author": {
                "username": "admin",
                "bio": "",
                "image": "https://static.productionready.io/images/smiley-cyrus.jpg",
                "following": false
            },
            "body": "57세 남자 환자가 오늘 내원해서 5달간 지속된 황달과 피로 증상을 호소하는데요, 어떤 처방을 주면 좋을까요??",
            "created": "48 minutes ago",
            "description": "황달 환자 처방 최신 경향",
            "favorited": false,
            "favoritesCount": 0,
            "slug": "-jbn4qd",
            "tagList": [
                "소화기내과",
                "암",
                "췌장"
            ],
            "title": "황달있는 환자에게 뭘 처방해야 하나요?",
            "modified": "48 minutes ago"
        },
        {
            "author": {
                "username": "admin",
                "bio": "",
                "image": "https://static.productionready.io/images/smiley-cyrus.jpg",
                "following": false
            },
            "body": "A 57-year-old male patient came to my clinic today, complaing about jaundice and malaise that existed for the last 5 months. What kind of medication should I give him?",
            "created": "53 minutes ago",
            "description": "Dealing with patient with possible pancreatic head cancer",
            "favorited": false,
            "favoritesCount": 0,
            "slug": "what-medication-should-i-prescribe-to-patient-with-jaundice-0adb2r",
            "tagList": [
                "Gastrointestinal",
                "Cancer",
                "Pancrease"
            ],
            "title": "What medication should I prescribe to patient with jaundice?",
            "modified": "53 minutes ago"
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
