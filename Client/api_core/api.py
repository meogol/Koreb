"""
200 - OK (PACKAGE WAS TAKED)
409 - Conflict (TAKER HAS NO MATCH WITH SERVER)
418 - I'm teapot (CLIENT IS WORKING NOW)
"""

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DELAY = 0.01

isWork = False
server_pkg = []
taker_pkg = []


@app.route("/post_server_pkg/", methods=['POST'])
def post_server_pkg():
    """
    Принимает от Сервера
    """
    global server_pkg
    pkg = request.form.to_dict(flat=False)
    server_pkg = pkg["pkg"]  # list
    return "200"


@app.route("/post_taker_pkg/", methods=['POST'])
def post_taker_pkg():
    """
    Принимает от Тейкера и сравнивает с Сервером
    """
    global taker_pkg
    global server_pkg
    global isWork

    pkg = request.form.to_dict(flat=False)
    taker_pkg = pkg["pkg"]

    if isWork:
        return "418"
    else:
        isWork = True
        if(len(taker_pkg) == len(server_pkg)):
            for i in range(len(taker_pkg)):
                if(taker_pkg[i] != server_pkg[i]):
                    isWork = False
                    return "409"
            isWork = False
            return "200"
        else:
            isWork = False
            return "409"


if __name__ == '__main__':
    app.run()
