#!/usr/bin/python3
"""this module conatins a script which will
select all states from states table"""


from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import (create_engine)
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    first = session.query(State).first()
    if first is not None:
        print(f"{first.id}: {first.name}")
    else:
        print('Nothing')
