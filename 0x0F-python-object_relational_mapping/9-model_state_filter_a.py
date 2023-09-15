#!/usr/bin/python3
""" This script lists all state objects that contain 'a' """

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1],
                                   argv[2],
                                   argv[3]),
                           pool_pre_ping=True)

    create_session = sessionmaker(engine)
    session = create_session()

    data = (session.query(State)
            .filter(State.name.like('%a%')).order_by(State.id).all())

    print('\n'.join(f"{state.id}: {state.name}" for state in data))
