#!/usr/bin/python3
""" This script creates a new state and print the id """

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

        new_state = State(name="Louisiana")

        session.add(new_state)
        session.commit()

        print(new_state.id)

    except (Exception, IndexError) as e:
        print(e)
