import requests
from flask import Flask, request
from flask_cors import CORS

if __name__ == '__main__':
    aaa = dict()
    aaa['a'] = [1, 2, 3]
    a = requests.post("http://127.0.0.1:5000/post_command/", data=aaa)
    requests.post("http://127.0.0.1:5000/post_pkg/", data={'ip': '56', 'pkg': '78'})
