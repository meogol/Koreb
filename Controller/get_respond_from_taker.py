from flask import Flask, request
from flask_cors import CORS
from Server.server import Server
app = Flask(__name__)
CORS(app)


@app.route("/taker_respond/", methods=['POST'])
def respond():
    """
    Get an respond from taker
    """
    respond_dict = request.form.to_dict(flat=False)
    respond = respond_dict["status"] #str

    Server.run()

    return 1

def run():
    app.run()

if __name__ == '__main__':
    app.run()


