# Flask skeleton

Template to starting a flask application more easily

- Flask
- Flask-WTF
- MongoDB
- Redis
- Google OAuth

## How to begin

```bash
git clone git@github.com:dev4hobby/flask-skeleton.git
cd flask-skeleton
pip install -r requirements.txt

# Edit config.dev.json
## Change the values of the variables
## Get GOOGLE_CLIENT_* from https://console.developers.google.com/apis/credentials

# Develop
python app.py
# or...
# gunicorn app:app --bind 0.0.0.0:5000
```

### config.*.json

```json
{
  "MONGO_HOST":"remote database url without protocol",
  "MONGO_PORT":"27017",
  "MONGO_USER":"username",
  "MONGO_PASSWORD":"password",
  "MONGO_NAME":"database_name",
  "GOOGLE_CLIENT_ID":"",
  "GOOGLE_CLIENT_SECRET":"",
  "REDIS_EXPIRE": 3600,
  "REDIS_HOST":"localhost",
  "REDIS_PORT":"6379",
  "REDIS_PASSWORD":""
}
```

## Deploy to heroku

Create `Procfile`

```json
web: gunicorn app:app --bind 0.0.0.0:${PORT}
```
