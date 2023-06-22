from flask import render_template, url_for, request, redirect, jsonify
import enum
from app import app


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


@app.route('/tank_control/', methods=['GET'])
def tank_control():
    return render_template('tank_control.html')


@app.route('/gpt/', methods=['GET'])
def gpt():
    return render_template('chat_gpt.html')
