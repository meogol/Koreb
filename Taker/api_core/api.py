
import werkzeug.datastructures
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/post_command/", methods=['POST'])
def post_command():

    command_dict = request.form
    new_dict = command_dict.to_dict(flat=False)

    print()

    print(new_dict)

    return 1


@app.route("/post_pkg/", methods=['POST'])
def post_pkg():

    ip = str(request.form["ip"])    #string
    pkg = str(request.form["pkg"])    #string

    print()
    print(ip)
    print()
    print(pkg)

    return 1


if __name__ == '__main__':
    app.run()
