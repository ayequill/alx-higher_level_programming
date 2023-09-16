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

        state = State(name="California")
        city = City(name="San Francisco", state=state)

        session.add(state, city)
        session.commit()
    except (Exception, IndexError) as e:
        print(e)
