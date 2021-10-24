from apps import app
from flask_cors import CORS

if __name__ == "__main__":
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.run(debug=True, host="0.0.0.0", port=5000)
