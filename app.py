from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/health', methods=["GET","POST"])
def health():
    if request.method=="GET":
        return jsonify(status="ok",method="GET"),200
    if request.method=="POST":
        return jsonify(status="ok",method="POST"),200


