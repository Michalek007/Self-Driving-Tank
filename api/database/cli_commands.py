from app import app, bcrypt, datetime
from database import *


@app.cli.command('db_create')
def db_create():
    """ Create all database tables. """
    db.create_all()
    print('Database created!')


@app.cli.command('db_drop')
def db_drop():
    """ Drops all database tables. """
    db.drop_all()
    print('Database dropped!')


@app.cli.command('db_seed')
def db_seed():
    """ Seeds database with default data. """
    user = User(username='admin', pw_hash=bcrypt.generate_password_hash('admin'))

    time = datetime.now()
    acc = Acceleration(date=time, x_axis=0, y_axis=0, z_axis=0)
    pos = Position(date=time, x=0, y=0, z=0)
    vel = Velocity(date=time, x_axis=0, y_axis=0, z_axis=0)

    db.session.add(user)
    db.session.add(acc)
    db.session.add(pos)
    db.session.add(vel)

    db.session.commit()
    print('Database seeded!')
