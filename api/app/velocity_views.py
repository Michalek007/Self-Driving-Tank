from flask import render_template, url_for, request, redirect, jsonify
from datetime import datetime

from app import app, bcrypt
from database import *


@app.route('/velocity/<int:vel_id>/', methods=['GET'])
@app.route('/velocity/', methods=['GET'])
def velocity(vel_id: int = None):
    if vel_id is None:
        velocity_list = Velocity.query.all()
        return jsonify(velocity=velocity_schema_many.dump(velocity_list))
    velocity_obj = Velocity.query.filter_by(id=vel_id).first()
    if velocity_obj:
        return jsonify(velocity=velocity_schema.dump(velocity_obj))
    else:
        return jsonify(message='There is no velocity with that id'), 404


@app.route('/get_velocity/', methods=['GET'])
def get_velocity():
    velocity_obj = Velocity.query.order_by(Velocity.id.desc()).first()
    calculated_vel = (velocity_obj.x_axis ** 2 + velocity_obj.y_axis ** 2) ** 0.5
    return jsonify(value=calculated_vel, time=velocity_obj.date)
