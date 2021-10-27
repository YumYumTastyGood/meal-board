from apps import app
from flask_cors import CORS

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    CORS(app, support_credentials=True)
