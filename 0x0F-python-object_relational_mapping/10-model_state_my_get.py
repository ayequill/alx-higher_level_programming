#!/usr/bin/python3
""" This script lists print the id of the state found """

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(argv[1],
                                       argv[2],
                                       argv[3]))

        Base.metadata.create_all(engine)
        create_session = sessionmaker(bind=engine)
        session = create_session()

        states = (session.query(State)
                  .filter(State.name == argv[4]).order_by(State.id))

        if states.count() < 1:
            print("Not found")
        else:
            for state in states:
                print(state.id)

    except (Exception, IndexError) as e:
        print(e)
