from flask import render_template, url_for, request, redirect, jsonify
from datetime import datetime

from app import app, bcrypt
from database import *


@app.route('/position/<int:pos_id>/', methods=['GET'])
@app.route('/position/', methods=['GET'])
def position(pos_id: int = None):
    if pos_id is None:
        position_list = Position.query.all()
        return jsonify(position=position_schema_many.dump(position_list))
    position_obj = Position.query.filter_by(id=pos_id).first()
    if position_obj:
        return jsonify(position=position_schema.dump(position_obj))
    else:
        return jsonify(message='There is no position with that id'), 404


@app.route('/add_position/', methods=['POST'])
def add_position():
    position_obj = Position(date=datetime.now(),
                            x=request.args.get('x'),
                            y=request.args.get('y'),
                            z=request.args.get('z'))
    db.session.add(position_obj)
    db.session.commit()
    return jsonify(message='You added position'), 201


@app.route('/delete_position/<int:pos_id>/', methods=['DELETE'])
def delete_position(pos_id: int = None):
    if pos_id is None:
        return jsonify(message='There is no position with that id'), 404
    position_obj = Position.query.filter_by(id=pos_id).first()
    if position_obj:
        db.session.delete(position_obj)
        db.session.commit()
        return jsonify(message='You deleted position with id: ' + str(pos_id)), 202
    else:
        return jsonify(message='There is no position with that id'), 404


@app.route('/get_position/', methods=['GET'])
def get_position():
    position_obj = Position.query.order_by(Position.id.desc()).first()
    return jsonify(x=position_obj.x, y=position_obj.y)
