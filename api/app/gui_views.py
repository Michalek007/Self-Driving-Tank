from flask import render_template, url_for, request, redirect, jsonify

from app import app


@app.route('/controls/', methods=['GET'])
def controls():
    return render_template('controls.html')


@app.route('/graphs/', methods=['GET'])
def graphs():
    return render_template('graphs.html')


@app.route('/acc_table/', methods=['GET'])
def acc_table():
    return render_template('acc_table.html')


@app.route('/velocity_table/', methods=['GET'])
def velocity_table():
    return render_template('velocity_table.html')


@app.route('/position_table/', methods=['GET'])
def position_table():
    return render_template('position_table.html')
