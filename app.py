from apps import app
from os import urandom
from flask_cors import CORS

if __name__ == "__main__":
    app.secret_key = urandom(12)
    app.config["SESSION_COOKIE_NAME"] = "google-login-session"
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=5)
    CORS(app, support_credentials=True)
    app.run(host="0.0.0.0", port=5000, debug=True)
