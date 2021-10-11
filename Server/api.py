from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/logging/", methods=['POST'])
def logging():
    """
    Get an error and displaying it into logs
    """
    message = request.form.to_dict(flat=False)
    error = message["error"] #str

    if error == 100: #process corrupted error
        app.logger.error("The error 100 occurred: "
                         "process corrupted")
    elif error == 404: #command lost error
        app.logger.error("The error 404 occurred:"
                         "commands lost ")
    elif error == 200: #Client is working
        app.logger.error("The error 200 occurred: "
                         "Client is working right now")
    elif error == 303: #Client doesn't responding
        app.logger.error("The error 303 occurred:"
                         "Client doesn't responding")


    return 1



