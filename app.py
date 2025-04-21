from flask import Flask
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/')
def call_api():
    res = requests.get('https://en.wikipedia.org/wiki/Valorant')
    if res.status_code == 200:
        return {"message":res.text}
    elif res.status_code == 404:
        return {"message":"Something went wrong"}, 404
    else:
        return {"message":"Server Error"}, 500
    
