from flask import Flask

from routes import init_api_routes
from flask_cors import CORS

# create the Flask application
app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'Hello from the secret world of Flask! ;)'

init_api_routes(app)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
