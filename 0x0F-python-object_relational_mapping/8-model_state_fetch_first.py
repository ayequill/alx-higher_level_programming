#!/usr/bin/python3
""" This script lists the first state object from the db hbtn_0e_6_usa"""

from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1],
                                   argv[2],
                                   argv[3]),
                           pool_pre_ping=True)

    # Base.metadata.create_all(engine)

    create_session = sessionmaker(bind=engine)
    session = create_session()

    state = session.query(State).first()

    print(f"{state.id}: {state.name}")

    session.close()
