from flask import render_template, url_for, request, redirect, jsonify
from datetime import datetime

from app import app, bcrypt
from database import *


TIME = 0


@app.route('/acc/<int:acc_id>/', methods=['GET'])
@app.route('/acc/', methods=['GET'])
def acc(acc_id: int = None):
    """ Returns acc with given id or if not specified list of all acc objects from database.
        Input args: /id/.
        Output keys: acc {x_axis, y_axis, z_axis}.
    """
    if acc_id is None:
        acc_list = Acceleration.query.all()
        return jsonify(acc=acceleration_schema_many.dump(acc_list))
    acc_obj = Acceleration.query.filter_by(id=acc_id).first()
    if acc_obj:
        return jsonify(acc=acceleration_schema.dump(acc_obj))
    else:
        return jsonify(message='There is no acc with that id'), 404


@app.route('/add_acc/', methods=['POST'])
def add_acc():
    """ POST method.
        Adds acc to database. Calculates velocity and position depending on current acc data and last saved data in database.
        Input args: x_axis, y_axis, z_axis.
    """
    global TIME
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

    acc_obj = Acceleration(date=TIME,
                           x_axis=acc_x,
                           y_axis=acc_y,
                           z_axis=acc_z)
    pos_last_one = Position.query.order_by(Position.id.desc()).first()
    vel_last_one = Velocity.query.order_by(Velocity.id.desc()).first()
    acc_last_one = Acceleration.query.order_by(Acceleration.id.desc()).first()

    t = (TIME - datetime.strptime(acc_last_one.date, '%Y-%m-%d %H:%M:%S.%f')).microseconds * 1000000
    x = 0.5 * float(acc_obj.x_axis) * t * t + pos_last_one.x + t*float(vel_last_one.x_axis)
    y = 0.5 * float(acc_obj.y_axis) * t * t + pos_last_one.y + t*float(vel_last_one.y_axis)
    # z = 0.5 * float(acc.z_axis) * t * t + pos_last_one.z + t*float(vel.z_axis)

    position_obj = Position(date=TIME,
                            x=x,
                            y=y,
                            z=0)

    if -1.5 <= acc_obj.x_axis <= 1.5:
        vel_x = 0
    else:
        vel_x = float(acc_obj.x_axis) * t + vel_last_one.x_axis
    if -1.5 <= acc_obj.y_axis <= 1.5:
        vel_y = 0
    else:
        vel_y = float(acc_obj.y_axis) * t + vel_last_one.y_axis

    # vel_z = float(acc.z_axis) * t + vel.z_axis

    velocity_obj = Velocity(date=TIME,
                            x_axis=vel_x,
                            y_axis=vel_y,
                            z_axis=0)

    db.session.add(velocity_obj)
    db.session.add(position_obj)
    db.session.add(acc_obj)
    db.session.commit()
    return jsonify(message='You added acc'), 201


@app.route('/delete_acc/<int:acc_id>/', methods=['DELETE'])
def delete_acc(acc_id: int = None):
    """ DELETE method.
        Delete acc with given id.
        Input args: /id/.
    """
    if acc_id is None:
        return jsonify(message='There is no acc with that id'), 404
    acc_obj = Acceleration.query.filter_by(id=acc_id).first()
    if acc_obj:
        db.session.delete(acc_obj)
        db.session.commit()
        return jsonify(message='You deleted acc with id: ' + str(acc_id)), 202
    else:
        return jsonify(message='There is no acc with that id'), 404


@app.route('/get_acc/', methods=['GET'])
def get_acc():
    """ Returns current net acceleration (last saved in database)
        calculated according to equation: a = (ax^2 + ay^2) ^ 0.5.
        Output keys: value, time.
    """
    acc_obj = Acceleration.query.order_by(Acceleration.id.desc()).first()
    calculated_acc = (acc_obj.x_axis ** 2 + acc_obj.y_axis ** 2) ** 0.5
    return jsonify(value=calculated_acc, time=acc_obj.date)
