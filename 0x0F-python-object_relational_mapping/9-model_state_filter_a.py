#!/usr/bin/python3
""" This script lists all state objects that contain 'a' """

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

        data = (session.query(State)
                .filter(State.name.like('%a%')).order_by(State.id))

        for row in data:
            print("{}: {}".format(row.id, row.name))

    except (Exception, IndexError) as e:
        print(e)
