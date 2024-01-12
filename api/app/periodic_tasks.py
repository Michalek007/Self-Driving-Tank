from flask_apscheduler import APScheduler
from datetime import datetime
import random
import requests
import sqlalchemy.exc

from app import app
from database import db, Acceleration


scheduler = APScheduler()

# TODO: to improve
X_axis = 0
Y_axis = 0
Z_axis = 0
Iterator = 0


def add_acc_to_database():
    acc_obj = Acceleration(date=str(datetime.now()), x_axis=random.random(), y_axis=random.random(), z_axis=random.random())
    with app.app_context():
        try:
            db.session.add(acc_obj)
            db.session.commit()
            print('Acc saved!')
        except sqlalchemy.exc.IntegrityError:
            print('sqlalchemy.exc.IntegrityError -UNIQUE constraint failed: performance.date!')


def make_add_acc_request():
    global X_axis, Y_axis, Z_axis, Iterator
    with app.app_context():

        if Iterator < 10:
            X_axis = X_axis + 1
            Iterator = Iterator + 1
        else:
            X_axis = X_axis - 1
        payload = {'x_axis': X_axis,
                   'y_axis': Y_axis,
                   'z_axis': Z_axis}

        # payload = {'x_axis': round(random.random(), 2),
        #            'y_axis': round(random.random(), 2),
        #            'z_axis': round(random.random(), 2)}

        response = requests.post('http://127.0.0.1:5000/add_acc/', params=payload)
        print(response.json()['message'])


# @scheduler.task('cron', id='add_acc', second='*')
def add_acc():
    make_add_acc_request()
    # add_acc_to_database()


scheduler.init_app(app)
scheduler.start()
