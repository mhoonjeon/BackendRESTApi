# Charts

## 재진차트 생성하기

**Request**:

`POST` `api/v1/progress_charts/`
```json
Content-Type application/json
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

{
    "note": {
        "object": "value",
        "document": {
            "data": {},
            "nodes": [],
            "object": "document"
        }
    }
    "admission_chart": "89b22c32-ee98-4548-ab9e-df3fe215a59d"
}
```

**Parameters**:

Name       | 설명      | 타입   | 필수 | 주의
-----------|-----------|--------|------|------------
patient    |           | string | Yes  | patient의 id
subjective | 환자호소  | string | No   | 
objective  | 객관적수치| string | No   | 
assessment | 평가      | string | No   | 
plan       | 계획      | string | No   | 

**Response**:

```json
Content-Type application/json
201 Created

{
    "id": "8f9f251b-cf1b-40c6-989c-0b6959a79f97",
    "created": "2018-10-31T14:01:52+0000",
    "modified": "2018-10-31T14:01:52+0000",
    "note": {
        "object": "value",
        "document": {
            "data": {},
            "nodes": [],
            "object": "document"
        }
    }
    "admission_chart": "89b22c32-ee98-4548-ab9e-df3fe215a59d"
}
```

## 재진차트 리스트 가져오기

**Request**:

`GET` `api/v1/progress_charts/`
```json
Content-Type application/json
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

당장 쓸일이 없지만, 일단 개발의 편의성을 위해

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
            "id": "8f9f251b-cf1b-40c6-989c-0b6959a79f97",
            "note": {
                "object": "value",
                "document": {
                    "data": {},
                    "nodes": [],
                    "object": "document"
                    }
            }
            "created": "2018년 10월 31일",
            "modified": "2018년 10월 31일",
            "admission_chart": "89b22c32-ee98-4548-ab9e-df3fe215a59d"
        },
        {
            "id": "ecd02b79-dc47-441e-941f-02b179cd3039",
            "note": {
                "object": "value",
                "document": {
                    "data": {},
                    "nodes": [],
                    "object": "document"
                    }
            }
            "created": "2018년 10월 31일",
            "modified": "2018년 10월 31일",
            "admission_chart": "89b22c32-ee98-4548-ab9e-df3fe215a59d"
        }
    ]
}
```
