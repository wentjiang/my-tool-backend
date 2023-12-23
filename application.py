from flask import Flask
from flask_cors import CORS
from python.tools import tools

app = Flask(__name__)
CORS(app)
app.register_blueprint(tools, url_prefix='/my-tool/v1-0')


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
