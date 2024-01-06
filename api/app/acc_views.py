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
        return jsonify(acc=acceleration_schema.dump(acc))
    else:
        return jsonify(message='There is no acc with that id'), 404


@app.route('/add_acc/', methods=['POST'])
def add_acc():
    global VELOCITY, TIME
    TIME = datetime.now()
    acc_x = float(request.args.get('x_axis'))/100
    acc_y = float(request.args.get('y_axis'))/100
    acc_z = float(request.args.get('z_axis'))/100
    if -20 > acc_x or acc_x > 20 or -1.5 < acc_x < 1.5:
        acc_x = 0
    if -20 > acc_y or acc_y > 20 or -1.5 < acc_y < 1.5:
        acc_y = 0
    if -20 > acc_z or acc_z > 20 or -1.5 < acc_z < 1.5:
        acc_z = 0

    acc = Acceleration(date=TIME,
                       x_axis=acc_x,
                       y_axis=acc_y,
                       z_axis=acc_z)
    pos_last_one = Position.query.order_by(Position.id.desc()).first()
    vel = Velocity.query.order_by(Velocity.id.desc()).first()
    acc_last_one = Acceleration.query.order_by(Acceleration.id.desc()).first()

    t = (TIME - datetime.strptime(acc_last_one.date, '%Y-%m-%d %H:%M:%S.%f')).microseconds * 1000000
    x = 0.5 * float(acc.x_axis) * t * t + pos_last_one.x + t*float(vel.x_axis)
    y = 0.5 * float(acc.y_axis) * t * t + pos_last_one.y + t*float(vel.y_axis)
    # z = 0.5 * float(acc.z_axis) * t * t + pos_last_one.z + t*float(vel.z_axis)

    position = Position(date=TIME,
                        x=x,
                        y=y,
                        z=0)

    if -1.5 <= acc.x_axis <= 1.5:
        vel_x = 0
    else:
        vel_x = float(acc.x_axis) * t + vel.x_axis
    if -1.5 <= acc.y_axis <= 1.5:
        vel_y = 0
    else:
        vel_y = float(acc.y_axis) * t + vel.y_axis

    # vel_z = float(acc.z_axis) * t + vel.z_axis

    velocity = Velocity(date=TIME,
                        x_axis=vel_x,
                        y_axis=vel_y,
                        z_axis=0)

    db.session.add(velocity)
    db.session.add(position)
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


@app.route('/get_acc/', methods=['GET'])
def get_acc():
    acc = Acceleration.query.order_by(Acceleration.id.desc()).first()
    calculated_acc = (acc.x_axis ** 2 + acc.y_axis ** 2) ** 0.5
    return jsonify(value=calculated_acc, time=acc.date)


@app.route('/acc_paginate/', methods=['GET'])
def acc_paginate():
    acc_list = Acceleration.query.paginate().items
    print(acc_list)
    print(Acceleration.query.paginate().total)
    return jsonify(acc=acceleration_schema_many.dump(acc_list))
