from sqlalchemy import Column, Integer, String, Float

from app import ma
from database import db


class Position(db.Model):
    """ Table for position data.
        Fields -> 'id', 'date', 'x', 'y', 'z'
    """
    __tablename__ = 'position'
    id = Column(Integer, primary_key=True)
    date = Column(String)
    x = Column(Float)
    y = Column(Float)
    z = Column(Float)


class PositionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'x', 'y', 'z')


position_schema = PositionSchema()
position_schema_many = PositionSchema(many=True)
