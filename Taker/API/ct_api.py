from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/post_command", methods=['POST'])
def post_command():
    pass
