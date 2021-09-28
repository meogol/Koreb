import requests
from flask import Flask, request
from flask_cors import CORS

if __name__ == '__main__':
    a = requests.post("http://127.0.0.1:5000/post_command/", data={'command_dict':"{'a': [1, 2, 3]}"})
    requests.post("http://127.0.0.1:5000/post_pkg/", data={'ip':'56', 'pkg':'78'})
