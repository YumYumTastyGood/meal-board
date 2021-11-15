# meal-board

`NEIS OpenAPI: 급식정보`를 활용한 무언가를 만들어보았어요  
급식정보 조회, 피드형 커뮤니티를 제공하는 서비스입니다.  

소셜 서비스로 확장할 예정입니다.

[Go to page](https://meal-board.herokuapp.com/)

## 사용기술

- Flask
  - Flask-WTF
  - Flask
- MongoDB
  - MongoEngine
- Redis
- Google OAuth2
  - session [Check issue](https://github.com/dev4hobby/flask-skeleton/issues/10)

만들면서 포스트를 작성하였다.  

- [Flask App의 디렉터리는 어떤 구조로 만들어야 좋을지 고민해보았습니다.](https://velog.io/@d3fau1t/Flask-App%EC%9D%98-%EB%94%94%EB%A0%89%ED%84%B0%EB%A6%AC%EB%8A%94-%EC%96%B4%EB%96%A4-%EA%B5%AC%EC%A1%B0%EB%A1%9C-%EB%A7%8C%EB%93%A4%EC%96%B4%EC%95%BC-%EC%A2%8B%EC%9D%84%EC%A7%80-%EA%B3%A0%EB%AF%BC%EC%9D%84-%EC%A2%80-%ED%95%B4%EB%B3%B4%EC%95%98%EC%8A%B5%EB%8B%88%EB%8B%A4)
- [Flask에서 유효성 검사를 어떻게하면 좋을지 고민해보았습니다.](https://velog.io/@d3fau1t/Flask%EC%97%90%EC%84%9C-%EC%9C%A0%ED%9A%A8%EC%84%B1%EA%B2%80%EC%82%AC-%EC%96%B4%EB%96%BB%EA%B2%8C-%ED%95%98%EB%A9%B4%EC%A2%8B%EC%9D%84%EA%B9%8C)
- [Flask에서 MongoDB를 어떻게 사용하면 좋을지 고민해보았습니다.](https://velog.io/@d3fau1t/Flask%EC%97%90%EC%84%9C-MongoDB%EB%A5%BC-%EC%96%B4%EB%96%BB%EA%B2%8C-%EC%82%AC%EC%9A%A9%ED%95%98%EB%A9%B4-%EC%A2%8B%EC%9D%84%EC%A7%80-%EA%B3%A0%EB%AF%BC%ED%95%B4%EB%B3%B4%EC%95%98%EC%8A%B5%EB%8B%88%EB%8B%A4)

## 환경구성 및 서비스 실행

```bash
git clone git@github.com:YumYumTastyGood/meal-board.git
cd meal-board
touch config.dev.json # 설정파일 생성
pip install -r requirements.txt
gunicorn app:app --bind 0.0.0.0:8086 --reload -w -1
```

### 설정파일 예시

config.dev.json

```json
{
  "MONGO_HOST":"MongoDB Host",
  "MONGO_USER":"MongoDB Username",
  "MONGO_PASSWORD":"MongoDB Password",
  "MONGO_NAME":"MongoDB Database",
  "GOOGLE_CLIENT_ID":"Google Client ID",
  "GOOGLE_CLIENT_SECRET":"Google Client Secret",
  "REDIS_EXPIRE": 3600,
  "REDIS_HIOST":"localhost",
  "REDIS_PORT":"6379",
  "REDIS_PASSWORD":"",
  "NEIS_SERVICE_INFO":"https://open.neis.go.kr/hub/mealServiceDietInfo",
  "NEIS_API_KEY":"NEIS API KEY",
  "SECRET":"**SECRET**"
}
```

상세정보는 별도관리

## 배포

Heroku에 배포하였다.

### Procfile

```bash
web: gunicorn -w 1 app:app --bind 0.0.0.0:${PORT}
```

session 이슈가 있어 스케일링을 하면 로그인 관련 기능에서 오류가 발생한다.
쿠키를 끼워넣던 로직을 수정하던 별도의 작업이 필요할듯.
