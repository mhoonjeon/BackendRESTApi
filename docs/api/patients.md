# Patients
환자 관련

## 환자 생성하기

**Request**:

`POST` `api/v1/patients/`
```json
Content-Type application/json
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

{
	"name": "류현진",
	"gender": "male",
    "age": 27
}
```

**Response**:

```json
Content-Type application/json
201 Created
{
    "id": "404b9569-f3f2-4062-bbf8-33274f11fc24",
    "name": "류현진",
    "gender": 0,  // 0은 남자, 1은 여자 Get에서는 male, female로 표시됨
    "age": 27
}
```

## 환자 리스트 불러오기

**Request**:

`GET` `api/v1/sentences/`
```json
Content-Type application/json
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```
**Response**:

```json
Content-Type application/json
200 OK

{
    "count": 4,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": "fdefbe82-3ae6-4eb1-b630-b3d189778b4d",
            "name": "Myong-Hoon Jeon",
            "gender": "male",
            "age": 23
        },
        {
            "id": "c614a508-793a-4ad9-8273-80084712f222",
            "name": "전명훈",
            "gender": "male",
            "age": 23
        },
        {
            "id": "a97cf41f-5f43-4584-8147-7b72902eb495",
            "name": "김인석",
            "gender": "male",
            "age": 23
        },
        {
            "id": "9fbb9bc9-7c0e-4a0a-b65f-6d188f33d180",
            "name": "허환",
            "gender": "male",
            "age": 23
        }
    ]
}
```
