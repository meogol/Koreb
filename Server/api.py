from flask import Flask, request
from flask_cors import CORS
from gevent.pywsgi import  WSGIServer


app = Flask(__name__)
CORS(app)


@app.route("/logs/", methods=['POST'])
def logs():
    """
    Get an error and displaying it into logs
    """
    res_dict = request.form.to_dict(flat=False)
    status = res_dict['status'] #str

    if status[0] == '100':  # process corrupted error
        app.logger.error("The error 100 occurred: "
                         "process corrupted")
    elif status[0] == '404':  # command lost error
        app.logger.error("The error 404 occurred:"
                         "commands lost ")
    elif status[0] == '200':  # Client is working
        app.logger.error("The error 200 occurred: "
                         "Client is working right now")
    elif status[0] == '303':  # Client doesn't responding
        app.logger.error("The error 303 occurred:"
                         "Client doesn't responding")
    else:
        return '1'

    return '1'

def run():
    http_server = WSGIServer(('127.0.0.1', 4999), app)
    http_server.serve_forever()
    app.run()

if __name__ == '__main__':
    app.run()
