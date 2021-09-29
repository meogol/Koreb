import werkzeug.datastructures
from flask import Flask, request
from flask_cors import CORS

from Taker.controller import Controller

app = Flask(__name__)
CORS(app)
controller = Controller()


@app.route("/post_command/", methods=['POST'])
def post_command():
    """
    Принимает дикт фгрегационных команд и их ключей
    """
    command_dict = request.form
    new_dict = command_dict.to_dict(flat=False)

    controller.update_graph(new_dict)
    print(new_dict)

    return "1"


@app.route("/post_pkg/", methods=['POST'])
def post_pkg():
    """
    принимает передатый пакет(лист)
    """
    ip = str(request.form["ip"])  # string
    pkg = str(request.form)  # list

    controller.analyse_command(ip, pkg)

    print(ip)
    print(pkg)

    return "1"


if __name__ == '__main__':
    app.run()
