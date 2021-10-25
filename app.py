from apps import app

if __name__ == "__main__":
    CORS(app, support_credentials=True)
    app.secret_key = urandom(12)
    app.config["SESSION_COOKIE_NAME"] = "google-login-session"
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=5)
    app.run(host="0.0.0.0", port=5000, debug=True)
