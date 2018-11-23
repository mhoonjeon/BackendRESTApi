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

Content-Type application/json
200 OK

{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "8bd53fdf-99ae-4bcb-ba3e-218f2b89c4a1",
            "patient": {
                "id": "9ea88e27-1aa5-4046-86b6-fa64d75059ce",
                "name": "전명훈",
                "gender": "male",
                "age": 23
            },
            "progress_charts": [],
            "created": "2018년 10월 31일",
            "modified": "2018년 10월 31일",
            "cc": "복통",
            "pi": "내원 3일전부터 속이 쓰리고 배가 아파옴",
            "pmhx": "당뇨, 고혈압, 3년 전 췌장염",
            "psxhx": "수술한 적 없음",
            "fhx": "어머니 위암",
            "shx": "술, 담배 안함, 직업: 무직",
            "medications": "고혈압, 당뇨 약 복용 중",
            "ros": "배가 살살 아프고 하복부 통증",
            "pe": "rebound tenderness, 배꼽 주위 압통",
            "labs": "AST, ALT 상승",
            "dx": "r/o 충수돌기염",
            "plan": "복부초음파"
        },
        {
            "id": "89b22c32-ee98-4548-ab9e-df3fe215a59d",
            "patient": {
                "id": "9ea88e27-1aa5-4046-86b6-fa64d75059ce",
                "name": "전명훈",
                "gender": "male",
                "age": 23
            },
            "progress_charts": [
                {
                    "id": "ecd02b79-dc47-441e-941f-02b179cd3039",
                    "created": "2018년 10월 31일",
                    "modified": "2018년 10월 31일",
                    "subjective": "나아짐",
                    "objective": "좋아진듯",
                    "assessment": "복통",
                    "plan": "침치료",
                    "admission_chart": "89b22c32-ee98-4548-ab9e-df3fe215a59d"
                }
            ],
            "created": "2018년 10월 31일",
            "modified": "2018년 10월 31일",
            "cc": "배가 아파요",
            "pi": "",
            "pmhx": "",
            "psxhx": "",
            "fhx": "",
            "shx": "",
            "medications": "",
            "ros": "",
            "pe": "",
            "labs": "",
            "dx": "",
            "plan": ""
        }
    ]
}
```
