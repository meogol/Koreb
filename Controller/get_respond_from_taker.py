from flask import Flask, request
from flask_cors import CORS
import requests
from gevent.pywsgi import  WSGIServer

app = Flask(__name__)
CORS(app)


@app.route("/respond/", methods=['POST'])
def respond():
    """
    Get an respond from taker
    """
    res_dict = request.form.to_dict(flat=False)
    status = res_dict['status']  # str

    requests.post('http://127.0.0.1:4999/logs/', data={'status': status[0]})
    return 1

def run():
    '''
    Running 'app' server on 127.0.0.1:4998
    '''
    http_server = WSGIServer(('127.0.0.1', 4998), app)
    http_server.serve_forever()
    app.run()

if __name__ == '__main__':
    app.run()


