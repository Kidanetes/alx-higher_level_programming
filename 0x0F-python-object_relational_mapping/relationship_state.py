#!/usr/bin/python3
"""this module contains the definition of
state class"""


from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

a = MetaData()
Base = declarative_base(metadata=a)


class State(Base):
    """This class contains the defintion of state table """
    __tablename__ = "states"
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(50))
    cities = relationship("City", backref="states")
