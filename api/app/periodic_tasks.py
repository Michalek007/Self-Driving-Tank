import random
import requests
import sqlalchemy.exc
from flask_apscheduler import APScheduler
import psutil
from datetime import datetime

from app import app
from database import *

scheduler = APScheduler()


# X = 0
# Y = 0
# Z = 0
# I = 0
#
#
# @scheduler.task("cron", id="acc", second="*")
# def acc():
#     global X, Y, Z, I
#     # acc = Acceleration(date=str(datetime.now()), x_axis=random.random(),y_axis=random.random(),z_axis=random.random())
#     with app.app_context():
#         # payload = {'x_axis': round(random.random(), 2),
#         #            'y_axis': round(random.random(), 2),
#         #            "z_axis": round(random.random(), 2)}
#         # response = requests.post("http://127.0.0.1:5000/add_acc/", params=payload)
#         if I < 10:
#             X = X + 1
#             I = I + 1
#         else:
#             X = X - 1
#         payload = {'x_axis': X,
#                    'y_axis': Y,
#                    "z_axis": Z}
#         response = requests.post("http://127.0.0.1:5000/add_acc/", params=payload)
#         print(response.json()["message"])
#         # try:
#         #     db.session.add(acc)
#         #     db.session.commit()
#         #     print("Acc saved!")
#         # except sqlalchemy.exc.IntegrityError:
#         #     print("sqlalchemy.exc.IntegrityError -UNIQUE constraint failed: performance.date!")


scheduler.init_app(app)
scheduler.start()
