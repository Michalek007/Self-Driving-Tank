from sqlalchemy import Column, Integer, String, Float

from app import ma
from database import db


class Velocity(db.Model):
    __tablename__ = 'velocity'
    id = Column(Integer, primary_key=True)
    date = Column(String)
    x_axis = Column(Float)
    y_axis = Column(Float)
    z_axis = Column(Float)


class VelocitySchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'x_axis', 'y_axis', 'z_axis')


velocity_schema = VelocitySchema()
velocity_schema_many = VelocitySchema(many=True)
