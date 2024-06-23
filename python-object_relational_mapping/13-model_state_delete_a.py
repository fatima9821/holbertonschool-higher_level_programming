
#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter a"""

import sys
from model_state import Base, State
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

    # Query State objects with names containing the letter "a"
    states_to_delete = session.query(State).filter(
            State.name.like('%a%')).all()

    # Delete the State objects
    for state in states_to_delete:
        session.delete(state)

    # Commit the session to the database
    session.commit()

    # Close the session
    session.close()

