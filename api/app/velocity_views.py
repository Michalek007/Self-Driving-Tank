from flask import render_template, url_for, request, redirect, jsonify
from datetime import datetime
from app import app, bcrypt
from database import *


@app.route('/velocity/<int:id>/', methods=['GET'])
@app.route('/velocity/', methods=['GET'])
def velocity(id: int = None):
    if id is None:
        vel_list = Velocity.query.all()
        return jsonify(velocity=velocity_schema_many.dump(vel_list))
    vel = Velocity.query.filter_by(id=id).first()
    if vel:
        return jsonify(velocity=velocity_schema.dump(vel))
    else:
        return jsonify(message='There is no vel with that id'), 404


@app.route('/get_velocity/', methods=['GET'])
def get_velocity():
    vel = Velocity.query.order_by(Velocity.id.desc()).first()
    calculated_vel = (vel.x_axis ** 2 + vel.y_axis ** 2) ** 0.5
    return jsonify(value=calculated_vel, time=vel.date)
