
#!/usr/bin/python3
"""Changes the name of a State object from the database hbtn_0e_6_usa"""

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

    # Query the State object with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Change the name of the State object to "New Mexico"
    state_to_update.name = "New Mexico"

    # Commit the session to the database
    session.commit()

    # Close the session
    session.close()

