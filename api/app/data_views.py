from flask import render_template, url_for, request, redirect, jsonify
from datetime import datetime
from app import app, bcrypt
from database import *


@app.route('/acc/<int:id>/', methods=['GET'])
@app.route('/acc/', methods=['GET'])
def acc(id: int = None):
    if id is None:
        acc_list = Acceleration.query.all()
        return jsonify(acc=acceleration_schema_many.dump(acc_list))
    acc = Acceleration.query.filter_by(id=id).first()
    if note:
        return jsonify(acc=acceleration_schema.dump(note))
    else:
        return jsonify(message='There is no acc with that id'), 404


@app.route('/add_acc/', methods=['POST'])
def add_acc():
    acc = Acceleration(date=datetime.now(),
                       x_axis=request.args.get('x_axis'),
                       y_axis=request.args.get('y_axis'),
                       z_axis=request.args.get('z_axis'))
    db.session.add(acc)
    db.session.commit()
    return jsonify(message='You added acc.'), 201


@app.route('/delete_acc/<int:id>/', methods=['DELETE'])
def delete_acc(id: int = None):
    if id is None:
        return jsonify(message='There is no acc with that id'), 404
    acc = Acceleration.query.filter_by(id=id).first()
    if acc:
        db.session.delete(acc)
        db.session.commit()
        return jsonify(message='You deleted acc with id: ' + str(id)), 202
    else:
        return jsonify(message='There is no acc with that id'), 404


@app.route('/position/<int:id>/', methods=['GET'])
@app.route('/position/', methods=['GET'])
def position(id: int = None):
    if id is None:
        position_list = Position.query.all()
        return jsonify(position=position_schema_many.dump(position_list))
    position = Position.query.filter_by(id=id).first()
    if position:
        return jsonify(position=position_schema.dump(position))
    else:
        return jsonify(message='There is no position with that id'), 404


@app.route('/add_position/', methods=['POST'])
def add_position():
    position = Position(date=datetime.now(),
                        x=request.args.get('x'),
                        y=request.args.get('y'),
                        z=request.args.get('z'))
    db.session.add(position)
    db.session.commit()
    return jsonify(message='You added acc.'), 201


@app.route('/delete_position/<int:id>/', methods=['DELETE'])
def delete_position(id: int = None):
    if id is None:
        return jsonify(message='There is no position with that id'), 404
    position = Position.query.filter_by(id=id).first()
    if position:
        db.session.delete(position)
        db.session.commit()
        return jsonify(message='You deleted position with id: ' + str(id)), 202
    else:
        return jsonify(message='There is no position with that id'), 404


@app.route('/graphs/', methods=['GET'])
def graphs():
    return render_template('graphs.html')


TIME = 1
@app.route('/graphs/get_data/', methods=['GET'])
def get_data():
    global TIME
    TIME += 1
    acc = Acceleration.query.order_by(Acceleration.id.desc()).first()
    print(acc.x_axis)
    print(acc.date)
    return jsonify(value=TIME)