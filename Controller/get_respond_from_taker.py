from flask import Flask, request
from flask_cors import CORS
import requests
from gevent.pywsgi import WSGIServer

import Controller.controller

app = Flask(__name__)
CORS(app)
controller: Controller


@app.route("/respond/", methods=['POST'])
def respond():
    """
    Get an respond from taker
    """
    res_dict = request.form.to_dict(flat=False)
    command = res_dict['command']  # str
    status = res_dict['status']  # str

    latest_got_command = command[0]

    if status[0] == 'OK':
        pass
    else:
        if status[0] == '100':  # process corrupted error
            app.logger.error("The error 100 occurred: process corrupted\n"
                             "Reporting to server")
            requests.post('http://127.0.0.1:4999/logs/', data={'status': status[0]})
            return '1'

        elif status[0] == '404':  # command lost error
            app.logger.error("The error 404 occurred: commands lost\n"
                             "Resending command")
            controller.analyze_package(latest_got_command)
            return '1'

        elif status[0] == '202':  # Client is working
            app.logger.error("The error 202 occurred: Client is working right now")
            return '1'

        elif status[0] == '303':  # Client doesn't responding
            app.logger.error("The error 303 occurred: Client doesn't responding\n"
                             "Reporting to server")
            requests.post('http://127.0.0.1:4999/logs/', data={'status': status[0]})
            return '1'

        else:
            return '1'

    return '1'


def run(controller1: Controller):
    '''
    Running 'app' server on 127.0.0.1:4998
    '''

    global controller
    controller = controller1
    http_server = WSGIServer(('127.0.0.1', 4998), app)
    http_server.serve_forever()
    app.run()


if __name__ == '__main__':
    app.run()
