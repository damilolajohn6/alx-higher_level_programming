#!/usr/bin/python3
'''Script that lists all State objects that contain the letter
a from the database hbtn_0e_6_usa'''

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine_str = 'mysql+mysqldb://{}:{}@localhost/{}'\
                 .format(sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(engine_str, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)\
                    .filter(State.name.like('%a%'))\
                    .order_by(State.id)

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
