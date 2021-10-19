# meal-board

NEIS OpenAPI, 급식정보를 활용한 무언가를 만들고있어요..

## API

### 지역정보 조회

GET, `/school/location`

응답

```json
{
    "status_code": 200,
    "location": {
        "B10": "서울특별시교육청",
        "C10": "부산광역시교육청",
        ...
        "V10": "특수학교"
    }
}
```

### 학교 조회

GET `/school`  

Query Params

```json
{
  "location": "B10", // <String>
  "school": "가락고등학교" // <String>
}
```

요청 예시

> /school?location=B10&school=가락고등학교

응답 예시

```json
{
    "school_list": [
        {
            "region_code": "B10", // <String>
            "school_name": "가락고등학교", // <String>
            "school_code": "7010057", // <String>
            "school_establish_date": 19890428 // <Int>
        },
        ...
    ]
}
```

### 식사 정보 조회

GET `/meal`

Query Params

```json
{
    "begin": "20190101", // <String>
    "end": "20190102", // <String>
    "region_code": "B10", // <String>
    "school_code": "7010057" // <String>
}

```

요청 예시

> ?when=today&begin=20210901&end=20210903&region_code=B10&school_code=7010057

응답 예시

```json
{
    "result": {
        "20210901": {
            "MMEAL_SC_CODE": "2",
            "MMEAL_SC_NM": "중식",
            "DDISH_NM": [
                "칼슘찹쌀밥",
                ...
                "토마토카프리제"
            ]
        },
        "20210902": {
            "MMEAL_SC_CODE": "2",
            "MMEAL_SC_NM": "중식",
            "DDISH_NM": [
                "칼슘곡혼합잡곡밥",
                ...
                "옥수수콘샐러드"
            ]
        },
        ...
    }
}
```


## 환경구성 및 서비스 실행

```bash
git clone git@github.com:YumYumTastyGood/meal-board.git
cd meal-board
touch config.dev.json # 설정파일 생성
pip install -r requirements.txt
FLASK_APP=app.py flask run --reload
```

### 설정파일 예시

```json
{
  "MEALS_MONGO_HOST":"원격 데이터베이스 주소",
  "MEALS_MONGO_PORT":"27017",
  "MEALS_MONGO_USER":"mealboard",
  "MEALS_MONGO_PASSWORD":"패스워드",
  "MEALS_MONGO_COLLECTION":"mealboard"
}
```

상세정보는 별도관리
