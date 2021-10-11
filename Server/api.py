from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/trouble_message/", methods=['POST'])
def trouble_message():
    """
    Get an error and displaying it into logs
    """
    error_message = request.form
    app.logger.error("Error received: " + error_message)

    return 1



