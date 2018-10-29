# Sentences
문장 저장

## 문장 저장

**Request**:

`POST` `api/v1/sentences/`
```json
Content-Type application/json
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

{
	"raw": "배가 아파요",
	"category": "CC",
	"chart": "f7fedb8a-e8cd-4c88-8696-701248cfddfc",
}
```

**Parameters**:

Name       | 타입   | 필수 | 주의
-----------|--------|------|------------
raw        | string | Yes  |
category   | string | Yes  | 가능한 값: "CC", "PI", "PMH", "FH", "SH", "ROS"
chart      | string | Yes  |

**Response**:

```json
Content-Type application/json
201 Created

{
    "id": "42cf35a8-9ad4-4613-99c2-c741a62f24f9",
    "created": "2018-10-29T14:44:12+0000",
    "modified": "2018-10-29T14:44:12+0000",
    "raw": "배가 아파요",
    "category": "CC",
    "chart": "f7fedb8a-e8cd-4c88-8696-701248cfddfc"
}
```

## 문장 저장(여러 개의 문장 한번에)

**Request**:

`POST` `api/v1/sentences/`
```json
Content-Type application/json
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
[
    {
        "chart": "f7fedb8a-e8cd-4c88-8696-701248cfddfc",  // chart.id
        "raw": "머리가 아파요",
        "category": "CC"
    },
    {
        "chart": "f7fedb8a-e8cd-4c88-8696-701248cfddfc",  // chart.id
        "raw": "기침이 나요",
        "category": "PI"
    },
    {
        "chart": "f7fedb8a-e8cd-4c88-8696-701248cfddfc",  // chart.id
        "raw": "10년전부터 당뇨가 있어요.",
        "category": "PMH"
    }
]
```
**Response**:

```json
Content-Type application/json
201 Created

[
    {
        "id": "15b40aae-8265-4a8f-8bcf-a3d29c5974c9",
        "created": "2018-10-29T15:13:49+0000",
        "modified": "2018-10-29T15:13:49+0000",
        "raw": "배가 아파요",
        "category": "CC",
        "chart": "f7fedb8a-e8cd-4c88-8696-701248cfddfc"
    },
    {
        "id": "4f221581-0dbf-4c51-b7d8-fcd8c0a65a81",
        "created": "2018-10-29T15:13:49+0000",
        "modified": "2018-10-29T15:13:49+0000",
        "raw": "기침이 나요",
        "category": "PI",
        "chart": "f7fedb8a-e8cd-4c88-8696-701248cfddfc"
    },
    {
        "id": "4ddb9694-479c-49ed-a82c-86ea06672e95",
        "created": "2018-10-29T15:13:49+0000",
        "modified": "2018-10-29T15:13:49+0000",
        "raw": "10년년전부터 당뇨가 있었어요",
        "category": "PMH",
        "chart": "f7fedb8a-e8cd-4c88-8696-701248cfddfc"
    }
]
```
