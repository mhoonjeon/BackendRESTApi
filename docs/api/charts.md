# Charts

## 차트 생성하기

**Request**:

`POST` `api/v1/charts/`
```json
Content-Type application/json
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

{
	"patient": "c614a508-793a-4ad9-8273-80084712f222",
}
```

**Parameters**:

Name       | Nested    | 타입   | 필수 | 주의
-----------|-----------|--------|------|------------
patient    |           | string | Yes  | patient의 id

**Response**:

```json
Content-Type application/json
201 Created

{
    "id": "75d9db76-3c3f-4232-b910-6de1a0d97c36",
    "created": "2018-10-29T11:04:50+0000",
    "modified": "2018-10-29T11:04:50+0000",
    "patient": "c614a508-793a-4ad9-8273-80084712f222"
}
```

## 차트 리스트 가져오기

**Request**:

`GET` `api/v1/charts/`
```json
Content-Type application/json
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```
**Query Parameter(선택사항)**:

`GET` `api/v1/charts/?created_today=true`로 요청을 날리면 오늘 생성된 차트만 필터링 해준다.

**Response**:

```json
Content-Type application/json
200 OK

{
    "count": 6,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "f7fedb8a-e8cd-4c88-8696-701248cfddfc",
            "patient": {
                "id": "80a02012-eadc-4f11-b21b-92f7de9eee71",
                "name": "전승훈",
                "gender": "male",
                "age": 11
            },
            "cc": "배가 아파요",
            "created": "2018년 10월 28일 09:58:09",
            "modified": "2018년 10월 28일 09:58:09"
        },
        {
            "id": "dee608f2-37c9-46f8-a413-a1eb8fb9fec3",
            "patient": {
                "id": "a97cf41f-5f43-4584-8147-7b72902eb495",
                "name": "김인석",
                "gender": "male",
                "age": 23
            },
            "cc": null,
            "created": "2018년 10월 29일 10:41:33",
            "modified": "2018년 10월 29일 10:41:33"
        },
        {
            "id": "adbe6eed-09ac-4773-9c0d-e6294f1994b5",
            "patient": {
                "id": "9fbb9bc9-7c0e-4a0a-b65f-6d188f33d180",
                "name": "허환",
                "gender": "male",
                "age": 23
            },
            "cc": null,
            "created": "2018년 10월 29일 00:54:28",
            "modified": "2018년 10월 29일 00:54:28"
        },
        {
            "id": "a6d40809-af34-4563-8b8b-184cef78b005",
            "patient": {
                "id": "c614a508-793a-4ad9-8273-80084712f222",
                "name": "전명훈",
                "gender": "male",
                "age": 23
            },
            "cc": null,
            "created": "2018년 10월 28일 00:46:34",
            "modified": "2018년 10월 28일 00:46:34"
        },
        {
            "id": "75d9db76-3c3f-4232-b910-6de1a0d97c36",
            "patient": {
                "id": "c614a508-793a-4ad9-8273-80084712f222",
                "name": "전명훈",
                "gender": "male",
                "age": 23
            },
            "cc": null,
            "created": "2018년 10월 29일 11:04:50",
            "modified": "2018년 10월 29일 11:04:50"
        },
        {
            "id": "250aed5d-acc2-44d1-88af-5f3e9072d8cb",
            "patient": {
                "id": "85491ad5-4429-448b-af6e-f63f6de5e1ed",
                "name": "원지운",
                "gender": "male",
                "age": 23
            },
            "cc": null,
            "created": "2018년 10월 29일 10:11:34",
            "modified": "2018년 10월 29일 10:11:34"
        }
    ]
}
```
