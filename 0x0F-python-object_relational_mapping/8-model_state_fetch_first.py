#!/usr/bin/python3
""" This script lists the first state object from the db hbtn_0e_6_usa"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1],
                                   argv[2],
                                   argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    create_session = sessionmaker(bind=engine)
    session = create_session()

    state = session.query(State).order_by(State.id).first()

    # print(f"{state.id}: {state.name}" if state else "Nothing")
    print('{:d}: {:s}'.format(state.id, state.name) if state else "Nothing")

    session.close()
