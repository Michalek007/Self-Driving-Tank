from flask import render_template, url_for, request, redirect, jsonify
from datetime import datetime
from app import app, bcrypt
from database import *


VELOCITY = 0
TIME = 0


@app.route('/acc/<int:id>/', methods=['GET'])
@app.route('/acc/', methods=['GET'])
def acc(id: int = None):
    if id is None:
        acc_list = Acceleration.query.all()
        return jsonify(acc=acceleration_schema_many.dump(acc_list))
    acc = Acceleration.query.filter_by(id=id).first()
    if acc:
        return jsonify(acc=acceleration_schema.dump(note))
    else:
        return jsonify(message='There is no acc with that id'), 404


@app.route('/add_acc/', methods=['POST'])
def add_acc():
    global VELOCITY, TIME
    TIME = datetime.now()
    acc = Acceleration(date=TIME,
                       x_axis=request.args.get('x_axis'),
                       y_axis=request.args.get('y_axis'),
                       z_axis=request.args.get('z_axis'))
    # acc = Acceleration(date=0.1,
    #                    x_axis=request.args.get('x_axis'),
    #                    y_axis=request.args.get('y_axis'),
    #                    z_axis=request.args.get('z_axis'))
    # acc_last_one = Acceleration.query.order_by(Acceleration.id.desc()).first()
    pos_last_one = Position.query.order_by(Position.id.desc()).first()
    t = 0.1
    x = 0.5 * float(acc.x_axis) * t * t + pos_last_one.x
    y = 0.5 * float(acc.y_axis) * t * t + pos_last_one.y
    z = 0.5 * float(acc.z_axis) * t * t + pos_last_one.z
    position = Position(date=TIME,
                        x=x,
                        y=y,
                        z=z)
    db.session.add(position)
    db.session.add(acc)
    db.session.commit()

    calculated_acc = (acc.x_axis ** 2 + acc.y_axis ** 2) ** 0.5
    VELOCITY = VELOCITY + calculated_acc * t
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


@app.route('/graphs/get_data/', methods=['GET'])
def get_data():
    acc = Acceleration.query.order_by(Acceleration.id.desc()).first()
    print(acc.x_axis)
    print(acc.date)
    return jsonify(value=acc.x_axis)


@app.route('/get_acc/', methods=['GET'])
def get_acc():
    acc = Acceleration.query.order_by(Acceleration.id.desc()).first()
    calculated_acc = (acc.x_axis ** 2 + acc.y_axis ** 2) ** 0.5
    return jsonify(value=calculated_acc, time=acc.date)


@app.route('/get_velocity/', methods=['GET'])
def get_velocity():
    global VELOCITY, TIME
    return jsonify(value=VELOCITY, time=TIME)


@app.route('/get_position/', methods=['GET'])
def get_position():
    pos = Position.query.order_by(Position.id.desc()).first()
    return jsonify(x=pos.x, y=pos.y)

