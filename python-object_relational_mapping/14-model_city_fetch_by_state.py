
#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""

import sys
from model_city import Base, City
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Entry point main"""

    # Database connection
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine to the database
    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name)
    engine = create_engine(db)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all City objects from the database
    cities = session.query(City).order_by(City.id).all()

    # Print the results
    for city in cities:
        state_name = session.query(State).filter_by(
                id=city.state_id).first().name
        print("{}: ({}) {}".format(state_name, city.id, city.name))

    # Close the session
    session.close()

