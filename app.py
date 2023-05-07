import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
import json


load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/languages')
def get_languages():
    with open("1.txt") as f:
        languages = json.load(f)
    return jsonify(languages)


@app.route('/students')
def get_students():
    with open('2.txt', 'r') as f:
        data = json.load(f)
    return jsonify(data)


if __name__ == '__main__':
    app.run()
