import requests
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/post_command/", methods=['POST'])
def post_command():

    command_dict = request.args.get("command_dict")

    print()
    print(command_dict)

    return 1


@app.route("/post_pkg/", methods=['POST'])
def post_pkg():

    ip = request.args.get("ip")    #string
    pkg = request.args.get("pkg")    #string

    print()
    print(ip)
    print()
    print(pkg)

    return 1


if __name__ == '__main__':
    app.run()
