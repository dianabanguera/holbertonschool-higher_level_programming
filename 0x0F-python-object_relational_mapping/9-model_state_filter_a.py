#!/usr/bin/python3
"""Script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State)\
                   .filter(State.name.ilike('%a%'))\
                   .order_by(State.id)

    for instance in query:
        print('{}: {}'.format(instance.id, instance.name))

    session.close()
