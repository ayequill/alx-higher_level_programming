#!/usr/bin/python3
""" Deletes all state in the db """

if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from sys import argv
    from model_state import Base, State

    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(argv[1],
                                       argv[2],
                                       argv[3]))

        Base.metadata.create_all(engine)

        create_session = sessionmaker(engine)
        session = create_session()

        (session.query(State)
         .filter(State.name.like('%a%')).delete(synchronize_session=False))
        session.commit()

    except (Exception, IndexError) as e:
        print(e)
    finally:
        session.close()
