# Charts

## 질문

**Request**:

`POST` `api/v1/charts/`
```json
Content-Type application/json
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

{
	"patient": "9ea88e27-1aa5-4046-86b6-fa64d75059ce",
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
    "created": "2018-10-31T13:56:38+0000",
    "modified": "2018-10-31T13:56:38+0000",
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
    "plan": "복부초음파",
    "patient": "9ea88e27-1aa5-4046-86b6-fa64d75059ce"
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
