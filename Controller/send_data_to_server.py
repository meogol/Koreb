import requests

class SendDataToServer:
    @staticmethod
    def send_pakage(status):
        """
        Sends status to the server
        """
        requests.post(" http://127.0.0.1:5000/logging/", data={"status":status})

        return 1

