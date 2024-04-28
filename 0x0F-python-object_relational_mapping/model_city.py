#!/usr/bin/python3
"""this module contains the definition of
state class"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """This class contains the defintion of city table """
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State")
