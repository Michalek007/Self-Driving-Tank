from sqlalchemy import Column, Integer, String, Float

from app import ma
from database import db


class Acceleration(db.Model):
    """ Table for acceleration data.
        Fields -> 'id', 'date', 'x_axis', 'y_axis', 'z_axis'
    """
    __tablename__ = 'acceleration'
    id = Column(Integer, primary_key=True)
    date = Column(String)
    x_axis = Column(Float)
    y_axis = Column(Float)
    z_axis = Column(Float)


class AccelerationSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'x_axis', 'y_axis', 'z_axis')


acceleration_schema = AccelerationSchema()
acceleration_schema_many = AccelerationSchema(many=True)
