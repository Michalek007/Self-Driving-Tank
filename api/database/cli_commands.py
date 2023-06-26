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
    user = User(username='admin', pw_hash=bcrypt.generate_password_hash('admin'))

    acc = Acceleration(date=datetime.now(), x_axis=0, y_axis=0, z_axis=0)

    pos = Position(date=datetime.now(), x=0, y=0, z=0)

    db.session.add(user)
    db.session.add(acc)
    db.session.add(pos)

    db.session.commit()
    print('Database seeded!')
