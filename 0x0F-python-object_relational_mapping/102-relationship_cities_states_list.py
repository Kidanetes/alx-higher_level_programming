#!/usr/bin/python3
"""this module contain a script which print
all cities"""

from sqlalchemy.orm import sessionmaker, joinedload, relationship
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for i in (session.query(City).order_by(City.id)):
        print(f"{i.id}: {i.name} -> {i.state.name}")
