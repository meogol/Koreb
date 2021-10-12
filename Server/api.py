from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/show_logs/", methods=['POST'])
def show_logs():
    """
    Get an error and displaying it into logs
    """
    message = request.form
    status = message

    if status == '100':  # process corrupted error
        app.logger.error("The error 100 occurred: "
                         "process corrupted")
        print("The error 100 occurred: "
                         "process corrupted")
    elif status == '404':  # command lost error
        app.logger.error("The error 404 occurred:"
                         "commands lost ")
    elif status == '200':  # Client is working
        app.logger.error("The error 200 occurred: "
                         "Client is working right now")
    elif status == '303':  # Client doesn't responding
        app.logger.error("The error 303 occurred:"
                         "Client doesn't responding")
    else:
        return 200

    return 200

def run():
    app.run()

if __name__ == '__main__':
    app.run()
