#!/usr/bin/python3
""" Deletes all state in the db """

if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from sys import argv
    from model_city import City
    from model_state import Base, State

    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(argv[1],
                                       argv[2],
                                       argv[3]))

        Base.metadata.create_all(engine)

        create_session = sessionmaker(engine)
        session = create_session()

        data = (session.query(State.name, City.id, City.name)
                .filter(State.id == City.state_id))

        for row in data:
            print(f"{row[0]}: ({row[1]}) {row[2]}")

    except (Exception, IndexError) as e:
        print(e)
