# Charts

## 초진차트 생성하기

**Request**:

`POST` `api/v1/charts/`
```json
Content-Type application/json
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

{
    "patient": {
        "name": "이일호",
        "gender": 0,  // 0: 남자, 1: 여자
        "age": 23
    },
    "note": {
        "object": "value",
        "document": {
            "data": {},
            "nodes": [],
            "object": "document"
        }
    }
}
```

**Parameters**:

Name       | 설명      | 타입   | 필수 | 주의
-----------|-----------|--------|------|------------
patient    |           | string | Yes  | patient의 id
cc         | 주소증    | string | No   | 
pi         | 현병력    | string | No   | 
pmhx       | 과거력    | string | No   | 
psxhx      | 수술력    | string | No   | 
fhx        | 가족력    | string | No   | 
shx        | 사회력    | string | No   | 
medications| 약물복용력| string | No   | 
ros        | 환자호소  | string | No   | 
pe         | 신체진찰  | string | No   | 
dx         | 진단      | string | No   | 
plan       | 계획      | string | No   | 

**Response**:

```json
Content-Type application/json
201 Created

{
    "id": "8bd53fdf-99ae-4bcb-ba3e-218f2b89c4a1",
    "patient": {
        "id": "e82bddd4-a3fe-436f-9483-2604f6e32540",
        "name": "이일호",
        "gender": 0,
        "age": 23
    },
    "note": {
        "object": "value",
        "document": {
            "data": {},
            "nodes": [],
            "object": "document"
        }
    }
    "created": "2018-10-31T13:56:38+0000",
    "modified": "2018-10-31T13:56:38+0000",
}
```

## 초진차트 리스트 가져오기

**Request**:

`GET` `api/v1/charts/`
```json
Content-Type application/json
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```
**Query Parameter(선택사항)**:

`GET` `api/v1/charts/?patient=<patient_id>`로 요청을 날리면 특정 환자의 차트만 필터링 해준다.

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
            "note": {
                "object": "value",
                "document": {
                    "data": {},
                    "nodes": [],
                    "object": "document"
                }
            }
            "progress_charts": [],
            "created": "2018년 10월 31일",
            "modified": "2018년 10월 31일",
        },
        {
            "id": "89b22c32-ee98-4548-ab9e-df3fe215a59d",
            "patient": {
                "id": "9ea88e27-1aa5-4046-86b6-fa64d75059ce",
                "name": "전명훈",
                "gender": "male",
                "age": 23
            },
                "note": {
                    "object": "value",
                "document": {
                    "data": {},
                    "nodes": [],
                    "object": "document"
                }
            }
            "progress_charts": [
                {
                    "id": "ecd02b79-dc47-441e-941f-02b179cd3039",
                    "created": "2018년 10월 31일",
                    "modified": "2018년 10월 31일",
                    "note": {
                        "object": "value",
                        "document": {
                            "data": {},
                            "nodes": [],
                            "object": "document"
                    }
                    "admission_chart": "89b22c32-ee98-4548-ab9e-df3fe215a59d"
                }
            ],
            "created": "2018년 10월 31일",
            "modified": "2018년 10월 31일",
        }
    ]
}
```
