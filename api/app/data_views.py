import flask_jwt_extended
from flask import render_template, url_for, request, redirect, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_jwt_extended import set_access_cookies, unset_jwt_cookies
from datetime import datetime
from app import app, bcrypt
from database import *


@app.route('/acc/<int:id>/', methods=['GET'])
@app.route('/acc/', methods=['GET'])
def acc(id: int = None):
    if id is None:
        acc_list = Acceleration.query.all()
        return jsonify(acc=acceleration_schema_many.dump(acc_list))
    acc = Acceleration.query.filter_by(id=id).first()
    if note:
        return jsonify(acc=acceleration_schema.dump(note))
    else:
        return jsonify(message='There is no acc with that id'), 404


@app.route('/add_acc/', methods=['POST'])
def add_acc():
    acc = Acceleration(date=datetime.now(),
                       x_axis=request.args.get('x_axis'),
                       y_axis=request.args.get('y_axis'),
                       z_axis=request.args.get('z_axis'))
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
