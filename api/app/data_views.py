from flask import render_template, url_for, request, redirect, jsonify
from datetime import datetime
from app import app, bcrypt
from database import *


@app.route('/graphs/', methods=['GET'])
def graphs():
    return render_template('graphs.html')


@app.route('/data/', methods=['GET'])
def data():
    return render_template("data.html")


