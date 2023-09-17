#!/usr/bin/python3
""" Create State Cali with City San francisco """

if __name__ == "__main__":
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from sys import argv

    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(argv[1],
                                       argv[2],
                                       argv[3]))

        Base.metadata.create_all(engine)
        create_session = sessionmaker(bind=engine)
        session = create_session()

        states = (session.query(State).filter(State.cities)
                  .order_by(State.id, City.id))

        for state in states:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"    {city.id}: {city.name}")

    except (Exception, IndexError) as e:
        print(e)
