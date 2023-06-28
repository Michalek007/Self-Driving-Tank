from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy()
db.init_app(app)

from database.user import User, user_schema, users_schema
from database.acceleration import Acceleration, acceleration_schema, acceleration_schema_many
from database.position import Position, position_schema, position_schema_many
from database.velocity import Velocity, velocity_schema, velocity_schema_many
