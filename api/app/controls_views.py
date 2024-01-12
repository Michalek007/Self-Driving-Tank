from flask import render_template, url_for, request, redirect, jsonify
import enum
import requests

from app import app
from database import *


class State(enum.Enum):
    stop = 0
    forward = 1
    backward = 2
    right = 3
    left = 4
    forward_left = 5
    forward_right = 6
    backward_left = 7
    backward_right = 8


# STATE = State.stop
STATE = 0


@app.route('/get_action/', methods=['GET'])
def get_action():
    return jsonify(state=STATE), 200


@app.route('/update_state/<int:value>/', methods=['UPDATE'])
def update_state(value: int):
    # STATE = State(value)
    global STATE
    STATE = value
    return jsonify(message='You updated state!'), 202


@app.route('/get_action_sim/', methods=['GET'])
def get_action_sim():
    # TODO: to improve
    # for simulation purposes
    global STATE
    X = 0
    Y = 0
    Z = 9.81
    acc = Acceleration.query.order_by(Acceleration.id.desc()).first()
    value = 0.01
    with app.app_context():
        if STATE == 1:
            Y = value
        elif STATE == 2:
            Y = -value
        elif STATE == 3:
            X = value
        elif STATE == 4:
            X = -value
        elif STATE == 5:
            Y = value
            X = -value
        elif STATE == 6:
            Y = value
            X = value
        elif STATE == 7:
            Y = -value
            X = -value
        elif STATE == 8:
            Y = -value
            X = value
        else:
            pass
        if STATE != 0:
            payload = {'x_axis': acc.x_axis + X,
                       'y_axis': acc.y_axis + Y,
                       'z_axis': 9.81}
            response = requests.post('http://127.0.0.1:5000/add_acc/', params=payload)
        else:
            payload = {'x_axis': 0,
                       'y_axis': 0,
                       'z_axis': 0}
            response = requests.post('http://127.0.0.1:5000/add_acc/', params=payload)
            last_acc = Acceleration.query.order_by(Acceleration.id.desc()).first()
            velocity = Velocity(date=last_acc.date,
                                x_axis=0,
                                y_axis=0,
                                z_axis=9.81)
            db.session.add(velocity)
            db.session.commit()

    return jsonify(message='Success!')
