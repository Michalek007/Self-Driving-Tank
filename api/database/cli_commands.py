from app import app, bcrypt, datetime
from database import *


@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database created!')


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database dropped!')


@app.cli.command('db_seed')
def db_seed():
    user1 = User(username='first', pw_hash=bcrypt.generate_password_hash('1234'))
    user2 = User(username='second', pw_hash=bcrypt.generate_password_hash('1234'))
    user3 = User(username='third', pw_hash=bcrypt.generate_password_hash('1234'))

    acc1 = Acceleration(date=datetime.now(), x_axis=9.81, y_axis=9.72, z_axis=9.81)
    acc2 = Acceleration(date=datetime.now(), x_axis=9.81, y_axis=9.72, z_axis=9.81)
    acc3 = Acceleration(date=datetime.now(), x_axis=9.81, y_axis=9.72, z_axis=9.81)

    pos1 = Position(date=datetime.now(), x=0, y=0, z=0)
    pos2 = Position(date=datetime.now(), x=2, y=3, z=0)
    pos3 = Position(date=datetime.now(), x=4, y=5, z=0)

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)

    db.session.add(acc1)
    db.session.add(acc2)
    db.session.add(acc3)

    db.session.add(pos1)
    db.session.add(pos2)
    db.session.add(pos3)

    db.session.commit()
    print('Database seeded!')
