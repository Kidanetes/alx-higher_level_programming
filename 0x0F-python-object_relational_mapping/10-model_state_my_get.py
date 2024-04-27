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
    flag = 0
    for i in (session.query(State).filter(State.name == "{}".format(argv[4])).
              order_by(State.id)):
        print(f"{i.id}")
        flag = 1
    if flag == 0:
        print('Not found')
