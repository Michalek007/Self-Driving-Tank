from flask import render_template, url_for, request, redirect, jsonify
import enum
from app import app


class State(enum.Enum):
    left = 0
    right = 1
    forward = 2
    backward = 3
    stop = 4


STATE = State.stop


@app.route('/get_action/', methods=['GET'])
def get_action():
    return jsonify(state=STATE), 200


@app.route('/update_state/<int:value>/', methods=['UPDATE'])
def update_state(value: int):
    STATE = State(value)
    return jsonify(message='You updated state!'), 202
