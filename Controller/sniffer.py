from Controller.traffic_generator.trafficGenerator import TrafficGenerator
from flask import Flask, request
from flask_cors import CORS


class Sniffer:
    def __init__(self):
        self.traffgen = TrafficGenerator()

    def get_ip_command(self):
        return self.traffgen.get_ip_and_command


app = Flask(__name__)
CORS(app)


@app.route("/post_scene/", methods=['POST'])
def post_scene():
    """
    принимает сценарий и передает на тейкер
    """
    scen = request.form.to_dict(flat=False)  # list

    print(scen)

    return "1"


if __name__ == '__main__':
    app.run()
