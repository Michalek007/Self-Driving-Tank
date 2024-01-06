from flask import render_template, url_for, request, redirect, jsonify
from datetime import datetime
from app import app, bcrypt
from database import *


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
    return jsonify(message='You added position.'), 201


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


@app.route('/get_position/', methods=['GET'])
def get_position():
    pos = Position.query.order_by(Position.id.desc()).first()
    return jsonify(x=pos.x, y=pos.y)
